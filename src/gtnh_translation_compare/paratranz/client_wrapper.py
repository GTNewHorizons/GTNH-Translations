import asyncio
import os
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
            f"received a 429 response, "
            f"waiting {wait_seconds} seconds before retrying "
            f"for the { {2: '2nd', 3: '3rd'}.get(retry_state.attempt_number + 1)} time"
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

    # noinspection PyBroadException
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
            logger.info("get_all_files: cache hit")
            return cast(AllFilesCache, all_files_cache).all_files
        else:
            logger.info("get_all_files: cache miss")
            AllFilesCache.write(
                path=os.path.join(self.cache_dir, "all_files_cache.json"),
                etag=res.headers["ETag"],
                all_files=res.json(),
            )
        self._log_res("get_files", res)
        return [File.model_validate(f) for f in res.json()]

    @retry_after_429()
    async def get_file(self, file_id: int) -> File:
        res = await self.client.get(url=f"projects/{self.project_id}/files/{file_id}")
        self._log_res(f"get_file[file_id={file_id}]", res)
        return File.model_validate(res.json())

    @retry_after_429()
    async def _get_strings_by_page(
        self,
        sem: asyncio.Semaphore,
        file_id: int,
        page: int = 1,
        page_size: int = 800,
        page_count: Optional[int] = None,
    ) -> StringPage:
        async with sem:
            logger.info("[get_strings]started: file_id={}, page={}, page_count={}", file_id, page, page_count or "?")
            res = await self.client.get(
                url=f"projects/{self.project_id}/strings",
                params={
                    "file": file_id,
                    "page": page,
                    "pageSize": page_size,
                },
            )
            self._log_res(f"get_strings[file_id={file_id}, page={page}]", res)
            logger.info("[get_strings]finished: file_id={}, page={}, page_count={}", file_id, page, page_count or "?")
        return StringPage.model_validate(res.json())

    async def get_strings(self, file_id: int) -> List[StringItem]:
        # concurrency number
        sem = asyncio.Semaphore(10)

        strings: List[StringItem] = list()

        string_page = await self._get_strings_by_page(sem, file_id)
        page_count = string_page.page_count
        strings.extend(string_page.results)

        tasks = [
            self._get_strings_by_page(
                sem,
                file_id,
                page=page,
                page_count=page_count,
            )
            for page in range(2, page_count + 1)
        ]

        tasks_result: Sequence[StringPage] = await asyncio.gather(*tasks)
        logger.info("[get_strings]finished_all: file_id={}, page_count={}", file_id, page_count)
        for string_page in tasks_result:
            strings.extend(string_page.results)

        return strings

    async def upload_file(self, paratranz_file: ParatranzFile) -> None:
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
                assert isinstance(f.id, int)
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
        self._log_res(f"create_file[path={path}]", res)
        return File.model_validate(res.json()["file"]).id

    @retry_after_429()
    async def _update_file(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        res = await self.client.post(
            url=f"projects/{self.project_id}/files/{file_id}",
            files={"file": paratranz_file.file_to_be_uploaded},
        )
        if res.status_code != 413:
            self._log_res(f"update_file[file_id={file_id}]", res)
            return

        logger.warning(
            "update_file[file_id={}] failed with 413 Payload Too Large; falling back to per-string updates",
            file_id,
        )
        await self._update_file_by_strings(file_id, paratranz_file)

    async def _update_file_by_strings(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        old_strings = await self.get_strings(file_id)
        sync_plan = self._prepare_string_sync_plan(old_strings, paratranz_file)

        if len(sync_plan.removed_ids) > 0:
            await self.delete_strings(sync_plan.removed_ids)
        if len(sync_plan.added_strings) > 0:
            await self.create_strings(file_id, sync_plan.added_strings)
        if len(sync_plan.updated_strings) > 0:
            await self.upload_strings(sync_plan.updated_strings)

        if (
            len(sync_plan.removed_ids) == 0
            and len(sync_plan.added_strings) == 0
            and len(sync_plan.updated_strings) == 0
        ):
            logger.info("[update_file]no changed strings: file_id={}", file_id)
            return
        logger.info(
            "[update_file]string sync finished: file_id={}, removed={}, added={}, updated={}",
            file_id,
            len(sync_plan.removed_ids),
            len(sync_plan.added_strings),
            len(sync_plan.updated_strings),
        )

    @staticmethod
    def _prepare_string_sync_plan(
        old_strings: List[StringItem],
        paratranz_file: ParatranzFile,
    ) -> "ClientWrapper.StringSyncPlan":
        old_strings_map: dict[str, StringItem] = {s.key: s for s in old_strings}
        new_strings_map: dict[str, StringItem] = {s.key: s for s in paratranz_file.string_items}
        new_keys = {s.key for s in paratranz_file.string_items}
        old_keys = set(old_strings_map.keys())

        removed_ids: List[int] = []
        for removed_key in old_keys - new_keys:
            removed_id = old_strings_map[removed_key].id
            if removed_id is not None:
                removed_ids.append(removed_id)

        added_strings: List[StringItem] = []
        for added_key in new_keys - old_keys:
            new_string = new_strings_map[added_key]
            added_strings.append(
                StringItem(
                    key=new_string.key,
                    original=new_string.original,
                    translation=new_string.translation,
                    context=new_string.context,
                    stage=new_string.stage,
                )
            )

        updated_strings: List[StringItem] = []
        for s in paratranz_file.string_items:
            if s.key not in old_strings_map:
                continue
            old_string = old_strings_map[s.key]
            if old_string.original == s.original:
                # If the translation attribute is not empty, meaning that it is in non-automation
                # and is manually assigned, then that value prevails
                if not s.translation:
                    s.translation = old_string.translation
                    s.stage = 1
            s.id = old_string.id

            if ClientWrapper._is_string_changed(old_string, s):
                updated_strings.append(s)

        return ClientWrapper.StringSyncPlan(
            removed_ids=removed_ids,
            added_strings=added_strings,
            updated_strings=updated_strings,
        )

    @staticmethod
    def _is_string_changed(old_string: StringItem, new_string: StringItem) -> bool:
        return (
            old_string.original != new_string.original
            or old_string.translation != new_string.translation
            or old_string.context != new_string.context
            or old_string.stage != new_string.stage
        )

    @retry_after_429()
    async def _save_file_extra(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        res = await self.client.put(
            url=f"projects/{self.project_id}/files/{file_id}",
            json={"extra": paratranz_file.file_extra.model_dump()},
        )
        self._log_res(f"save_file_extra[file_id={file_id}]", res)

    async def upload_strings(self, strings: list[StringItem]) -> None:
        async def upload(_sem: asyncio.Semaphore, string: StringItem) -> None:
            async with _sem:
                await self._upload_string(string)

        # concurrency number
        sem = asyncio.Semaphore(10)
        tasks = [upload(sem, string) for string in strings]
        await asyncio.gather(*tasks)
        logger.info("[upload_strings]finished_all: strings_count={}", len(strings))

    async def create_strings(self, file_id: int, strings: list[StringItem]) -> None:
        async def create(_sem: asyncio.Semaphore, string: StringItem) -> None:
            async with _sem:
                await self._create_string(file_id, string)

        sem = asyncio.Semaphore(10)
        tasks = [create(sem, string) for string in strings]
        await asyncio.gather(*tasks)
        logger.info("[create_strings]finished_all: strings_count={}", len(strings))

    async def delete_strings(self, string_ids: list[int]) -> None:
        async def delete(_sem: asyncio.Semaphore, string_id: int) -> None:
            async with _sem:
                await self._delete_string(string_id)

        sem = asyncio.Semaphore(10)
        tasks = [delete(sem, string_id) for string_id in string_ids]
        await asyncio.gather(*tasks)
        logger.info("[delete_strings]finished_all: strings_count={}", len(string_ids))

    @retry_after_429()
    async def _create_string(self, file_id: int, string: StringItem) -> None:
        payload = string.model_dump(exclude={"id"}, exclude_none=True)
        payload["file"] = file_id
        res = await self.client.post(
            url=f"projects/{self.project_id}/strings",
            json=payload,
        )
        self._log_res(f"create_strings[file_id={file_id}, key={string.key}]", res)

    @retry_after_429()
    async def _upload_string(self, string: StringItem) -> None:
        res = await self.client.put(
            url=f"projects/{self.project_id}/strings/{string.id}",
            json=string.model_dump()
        )
        self._log_res(f"upload_strings[string_id={string.id}]", res)

    @retry_after_429()
    async def _delete_string(self, string_id: int) -> None:
        res = await self.client.delete(
            url=f"projects/{self.project_id}/strings/{string_id}",
        )
        self._log_res(f"delete_strings[string_id={string_id}]", res)

    @staticmethod
    def _log_res(request_name: str, res: Response) -> None:
        try:
            res.raise_for_status()
        except HTTPStatusError as e:
            logger.error("{}: {}", request_name, res)
            raise e
        logger.debug("{}: {}", request_name, res)
