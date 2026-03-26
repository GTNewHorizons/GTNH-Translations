import asyncio
import os
import re
from typing import Optional, List, Sequence, cast, Callable, NamedTuple

from asyncache import cached  # type: ignore[import]
from cachetools import LRUCache  # type: ignore[import]
from httpx import AsyncClient, Response, HTTPStatusError
from loguru import logger
from pydantic import BaseModel
from tenacity import retry, wait_fixed, stop_after_attempt, retry_if_exception, WrappedFn, RetryCallState

from gtnh_translation_compare.paratranz.types import File, StringItem, StringPage, ParatranzFile


def retry_after_429() -> Callable[[WrappedFn], WrappedFn]:
    wait_seconds = 60

    def is_http_429_error(exception: BaseException) -> bool:
        return isinstance(exception, HTTPStatusError) and exception.response.status_code == 429

    def before_sleep(retry_state: RetryCallState) -> None:
        logger.warning(
            f"received a 429 response, waiting {wait_seconds}s before retry "
            f"(attempt {retry_state.attempt_number + 1})"
        )

    return retry(
        retry=retry_if_exception(is_http_429_error),
        wait=wait_fixed(wait_seconds),
        stop=stop_after_attempt(3),
        before_sleep=before_sleep,
    )


class AllFilesCache(BaseModel):
    etag: str
    all_files: List[File]

    @classmethod
    def read(cls, path: str) -> Optional["AllFilesCache"]:
        try:
            with open(path, "r") as fp:
                result = cls.model_validate_json(fp.read())
                os.utime(path)
                return result
        except Exception:
            return None

    @classmethod
    def write(cls, path: str, etag: str, all_files: List[File]) -> None:
        with open(path, "w") as fp:
            fp.write(cls(etag=etag, all_files=all_files).model_dump_json())


class ClientWrapper:
    class StringSyncPlan(NamedTuple):
        removed_ids: List[int]
        added_strings: List[StringItem]
        updated_strings: List[StringItem]

    def __init__(self, client: AsyncClient, project_id: int, cache_dir: str) -> None:
        self.client = client
        self.project_id = project_id
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    @staticmethod
    def _sanitize_key(key: str) -> str:
        key = key.strip()
        key = re.sub(r"\|\s+", "|", key)
        return key

    @cached(cache=LRUCache(maxsize=1))  # type: ignore[misc]
    @retry_after_429()
    async def get_all_files(self) -> List[File]:
        cache_json_path = os.path.join(self.cache_dir, "all_files_cache.json")
        all_files_cache = AllFilesCache.read(cache_json_path)
        headers = {}
        if all_files_cache:
            headers["If-None-Match"] = all_files_cache.etag

        res = await self.client.get(url=f"projects/{self.project_id}/files", headers=headers)

        if res.status_code == 304:
            return cast(AllFilesCache, all_files_cache).all_files

        AllFilesCache.write(
            path=cache_json_path,
            etag=res.headers["ETag"],
            all_files=res.json(),
        )

        self._log_res("get_files", res)
        return [File.model_validate(f) for f in res.json()]

    @retry_after_429()
    async def get_file(self, file_id: int) -> File:
        res = await self.client.get(url=f"projects/{self.project_id}/files/{file_id}")
        self._log_res(f"get_file[{file_id}]", res)
        return File.model_validate(res.json())

    @retry_after_429()
    async def _get_strings_by_page(
        self,
        sem: asyncio.Semaphore,
        file_id: int,
        page: int = 1,
        page_size: int = 800,
    ) -> StringPage:
        async with sem:
            res = await self.client.get(
                url=f"projects/{self.project_id}/strings",
                params={"file": file_id, "page": page, "pageSize": page_size},
            )
            self._log_res(f"get_strings[{file_id}:{page}]", res)
        return StringPage.model_validate(res.json())

    async def get_strings(self, file_id: int) -> List[StringItem]:
        sem = asyncio.Semaphore(10)

        first = await self._get_strings_by_page(sem, file_id)
        strings = first.results
        page_count = first.page_count

        tasks = [
            self._get_strings_by_page(sem, file_id, page=p)
            for p in range(2, page_count + 1)
        ]
        pages = await asyncio.gather(*tasks)

        for p in pages:
            strings.extend(p.results)

        # normalization of ALL keys
        for s in strings:
            s.key = self._sanitize_key(s.key)

        return strings

    async def upload_file(self, paratranz_file: ParatranzFile) -> None:
        for s in paratranz_file.string_items:
            s.key = self._sanitize_key(s.key)

        file_id = await self._find_file_id_by_file(paratranz_file.file_name)

        if file_id is None:
            file_id = await self._create_file(paratranz_file)
        else:
            await self._update_file(file_id, paratranz_file)

        await self._save_file_extra(file_id, paratranz_file)

    async def _find_file_id_by_file(self, filename: str) -> Optional[int]:
        files = await self.get_all_files()
        for f in files:
            if f.name == filename:
                return f.id
        return None

    @retry_after_429()
    async def _create_file(self, paratranz_file: ParatranzFile) -> int:
        path = os.path.dirname(paratranz_file.file_name)
        res = await self.client.post(
            url=f"projects/{self.project_id}/files",
            data={"path": path},
            files={"file": paratranz_file.file_to_be_uploaded},
        )
        self._log_res("create_file", res)
        return File.model_validate(res.json()["file"]).id

    @retry_after_429()
    async def _update_file(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        old_strings = await self.get_strings(file_id)
        self._preserve_existing_manual_translations(old_strings, paratranz_file)

        res = await self.client.post(
            url=f"projects/{self.project_id}/files/{file_id}",
            files={"file": paratranz_file.file_to_be_uploaded},
        )

        if res.status_code != 413:
            self._log_res("update_file", res)
            return

        await self._update_file_by_strings(file_id, paratranz_file, old_strings)

    async def _update_file_by_strings(
        self,
        file_id: int,
        paratranz_file: ParatranzFile,
        old_strings: List[StringItem],
    ) -> None:
        plan = self._prepare_string_sync_plan(old_strings, paratranz_file)

        if plan.removed_ids:
            await self.delete_strings(plan.removed_ids)
        if plan.added_strings:
            await self.create_strings(file_id, plan.added_strings)
        if plan.updated_strings:
            await self.upload_strings(plan.updated_strings)

    @staticmethod
    def _prepare_string_sync_plan(
        old_strings: List[StringItem],
        paratranz_file: ParatranzFile,
    ) -> "ClientWrapper.StringSyncPlan":

        def norm(s: StringItem) -> str:
            return ClientWrapper._sanitize_key(s.key)

        old_map = {norm(s): s for s in old_strings}
        new_map = {norm(s): s for s in paratranz_file.string_items}

        old_keys = set(old_map.keys())
        new_keys = set(new_map.keys())

        removed_ids = [
            old_map[k].id for k in (old_keys - new_keys) if old_map[k].id is not None
        ]

        added_strings = [new_map[k] for k in (new_keys - old_keys)]

        updated_strings = []
        for k in new_keys & old_keys:
            new = new_map[k]
            old = old_map[k]

            new.id = old.id

            if old.original == new.original and not new.translation:
                new.translation = old.translation
                new.stage = 1

            if (
                old.original != new.original
                or old.translation != new.translation
                or old.context != new.context
                or old.stage != new.stage
            ):
                updated_strings.append(new)

        return ClientWrapper.StringSyncPlan(
            removed_ids, added_strings, updated_strings
        )

    @retry_after_429()
    async def _save_file_extra(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        res = await self.client.put(
            url=f"projects/{self.project_id}/files/{file_id}",
            json={"extra": paratranz_file.file_extra.model_dump()},
        )
        self._log_res("save_file_extra", res)

    async def upload_strings(self, strings: list[StringItem]) -> None:
        sem = asyncio.Semaphore(10)

        async def run(s: StringItem):
            async with sem:
                await self._upload_string(s)

        await asyncio.gather(*(run(s) for s in strings))

    async def create_strings(self, file_id: int, strings: list[StringItem]) -> None:
        sem = asyncio.Semaphore(10)

        async def run(s: StringItem):
            async with sem:
                await self._create_string(file_id, s)

        await asyncio.gather(*(run(s) for s in strings))

    async def delete_strings(self, ids: list[int]) -> None:
        sem = asyncio.Semaphore(10)

        async def run(i: int):
            async with sem:
                await self._delete_string(i)

        await asyncio.gather(*(run(i) for i in ids))

    @retry_after_429()
    async def _create_string(self, file_id: int, string: StringItem) -> None:
        payload = string.model_dump(exclude={"id"}, exclude_none=True)
        payload["file"] = file_id

        res = await self.client.post(
            url=f"projects/{self.project_id}/strings",
            json=payload,
        )

        self._log_res("create_string", res)

    @retry_after_429()
    async def _upload_string(self, string: StringItem) -> None:
        res = await self.client.put(
            url=f"projects/{self.project_id}/strings/{string.id}",
            json=string.model_dump(),
        )
        self._log_res("upload_string", res)

    @retry_after_429()
    async def _delete_string(self, string_id: int) -> None:
        res = await self.client.delete(
            url=f"projects/{self.project_id}/strings/{string_id}",
        )
        self._log_res("delete_string", res)

    @staticmethod
    def _log_res(name: str, res: Response) -> None:
        res.raise_for_status()
