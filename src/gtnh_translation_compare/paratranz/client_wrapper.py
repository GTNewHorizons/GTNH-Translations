import asyncio
import os
from functools import cached_property
from typing import Optional, List, Sequence

from httpx import AsyncClient, Response
from loguru import logger

from gtnh_translation_compare.paratranz.types import File, StringItem, StringPage, ParatranzFile


class ClientWrapper:
    def __init__(self, client: AsyncClient, project_id: int):
        self.client = client
        self.project_id = project_id

    async def _get_all_files(self) -> List[File]:
        res = await self.client.get(url=f"projects/{self.project_id}/files")
        self._log_res("get_files", res)
        return [File.model_validate(f) for f in res.json()]

    @cached_property
    def all_files(self) -> List[File]:
        return asyncio.run(self._get_all_files())

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
        file_id = self._find_file_id_by_file(paratranz_file.file_name)

        if file_id is None:
            file_id = await self._create_file(paratranz_file)
        else:
            await self._update_file(file_id, paratranz_file)

        await self._save_file_extra(file_id, paratranz_file)

    def _find_file_id_by_file(self, filename: str) -> Optional[int]:
        for f in self.all_files:
            if f.name == filename:
                assert isinstance(f.id, int)
                return f.id
        return None

    async def _create_file(self, paratranz_file: ParatranzFile) -> int:
        path = os.path.dirname(paratranz_file.file_name)
        res = await self.client.post(
            url=f"projects/{self.project_id}/files",
            data={"path": path},
            files={"file": paratranz_file.file_to_be_uploaded},
        )
        self._log_res(f"create_file[path={path}]", res)
        return File.model_validate(res.json()["file"]).id

    async def _update_file(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        old_strings = await self.get_strings(file_id)
        old_strings_map: dict[str, StringItem] = {s.key: s for s in old_strings}
        for s in paratranz_file.string_items:
            if s.key in old_strings_map and old_strings_map[s.key].original == s.original:
                # If the translation attribute is not empty, meaning that it is in non-automation
                # and is manually assigned, then that value prevails
                if not s.translation:
                    old_translation = old_strings_map[s.key].translation
                    s.translation = old_translation
                    s.stage = 1

        res = await self.client.post(
            url=f"projects/{self.project_id}/files/{file_id}",
            files={"file": paratranz_file.file_to_be_uploaded},
        )
        self._log_res(f"update_file[file_id={file_id}]", res)

    async def _save_file_extra(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        res = await self.client.put(
            url=f"projects/{self.project_id}/files/{file_id}",
            json={"extra": paratranz_file.file_extra.model_dump()},
        )
        self._log_res(f"save_file_extra[file_id={file_id}]", res)

    @staticmethod
    def _log_res(request_name: str, res: Response) -> None:
        if 400 <= res.status_code:
            logger.error("{}: {}", request_name, res)
            return
        logger.debug("{}: {}", request_name, res)
