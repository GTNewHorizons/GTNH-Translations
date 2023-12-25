import asyncio
import json
from functools import cached_property
from os import path
from typing import Optional, Any, List

from loguru import logger
from paratranz_client import Configuration, ApiClient, ApiResponse, StringItem, SaveFileRequest
from paratranz_client.api import FilesApi, StringsApi

from gtnh_translation_compare import settings
from gtnh_translation_compare.paratranz.converter import ParatranzFile
from gtnh_translation_compare.paratranz.file_extra import FileExtraSchema
from gtnh_translation_compare.paratranz.paratranz_cache import ParatranzCache
from gtnh_translation_compare.paratranz.paratranz_file_ref import ParatranzFileRef


class ClientWrapper:
    def __init__(self, config: Configuration, project_id: int):
        self.config = config
        self.project_id = project_id
        self.cache = ParatranzCache(settings.PARATRANZ_CACHE_DIR)

    async def _get_all_files(self) -> List[ParatranzFileRef]:
        async with ApiClient(self.config) as client:
            files_api = FilesApi(client)
            res = await files_api.get_files_with_http_info(project_id=self.project_id)
            self._log_res("get_files", res)
            data_with_extra = json.loads(res.raw_data)
            return [
                ParatranzFileRef(value=res.data[i], extra=data_with_extra[i]["extra"]) for i in range(len(res.data))
            ]

    @cached_property
    def all_files(self) -> List[ParatranzFileRef]:
        return asyncio.run(self._get_all_files())

    async def _get_strings_by_page(
        self,
        sem: asyncio.Semaphore,
        strings_api: StringsApi,
        file_id: int,
        page: int,
        page_size: int,
        page_count: int,
    ) -> list[StringItem]:
        async with sem:
            logger.info("[get_strings]started: file_id={}, page={}, page_count={}", file_id, page, page_count)
            res = await strings_api.get_strings_with_http_info(
                project_id=self.project_id,
                file=file_id,
                page=page,
                page_size=page_size,
            )
            self._log_res(f"get_strings[file_id={file_id}, page={page}]", res)
            logger.info("[get_strings]finished: file_id={}, page={}, page_count={}", file_id, page, page_count)
        return res.data.results

    async def get_strings(self, file_id: int) -> list[StringItem]:
        page = 1
        page_size = 800
        strings: list[StringItem] = list()

        async with ApiClient(self.config) as client:
            logger.info("[get_strings]started: file_id={}, page={}, page_count=?", file_id, page)
            strings_api = StringsApi(client)
            res = await strings_api.get_strings_with_http_info(
                project_id=self.project_id,
                file=file_id,
                page=page,
                page_size=page_size,
            )
            self._log_res(f"get_strings[file_id={file_id}, page={page}]", res)
            logger.info("[get_strings]finished: file_id={}, page={}, page_count=?", file_id, page)
            strings.extend(res.data.results)

            page_count = res.data.page_count

            # concurrency number
            sem = asyncio.Semaphore(10)

            tasks = [
                self._get_strings_by_page(
                    sem,
                    strings_api,
                    file_id,
                    page,
                    page_size,
                    page_count,
                )
                for page in range(2, page_count + 1)
            ]

            tasks_result = await asyncio.gather(*tasks)
            logger.info("[get_strings]finished_all: file_id={}, page_count={}", file_id, page_count)
            for page_strings in tasks_result:
                strings.extend(page_strings)

        return strings

    async def upload_file(self, paratranz_file: ParatranzFile) -> None:
        assert isinstance(paratranz_file.file_model.name, str)
        file_id = self._find_file_id_by_file(paratranz_file.file_model.name)

        if file_id is None:
            file_id = await self._create_file(paratranz_file)
        else:
            await self._update_file(file_id, paratranz_file)

        await self._save_file_extra(file_id, paratranz_file)

    def _find_file_id_by_file(self, filename: str) -> Optional[int]:
        for f in self.all_files:
            if f.value.name == filename:
                assert isinstance(f.value.id, int)
                return f.value.id
        return None

    async def _create_file(self, paratranz_file: ParatranzFile) -> int:
        async with ApiClient(self.config) as client:
            files_api = FilesApi(client)
            res = await files_api.create_file_with_http_info(
                project_id=self.project_id,
                file=paratranz_file.file,
                path=path.dirname(paratranz_file.file_model.name),
            )
            self._log_res(f"create_file[path={path.dirname(paratranz_file.file_model.name)}]", res)
            return res.data.file.id

    async def _update_file(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        old_strings = await self.get_strings(file_id)
        old_strings_map: dict[str, StringItem] = {s.key: s for s in old_strings if isinstance(s.key, str)}
        for s in paratranz_file.json_items:
            if s.key in old_strings_map and old_strings_map[s.key].original == s.original:
                # If the translation attribute is not empty, meaning that it is in non-automation
                # and is manually assigned, then that value prevails
                if not s.translation:
                    old_translation = old_strings_map[s.key].translation
                    if isinstance(old_translation, str):
                        s.translation = old_translation
                        s.stage = 1

        async with ApiClient(self.config) as client:
            files_api = FilesApi(client)
            res = await files_api.update_file_with_http_info(
                project_id=self.project_id, file_id=file_id, file=paratranz_file.file
            )
            self._log_res(f"update_file[file_id={file_id}]", res)

    async def _save_file_extra(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        async with ApiClient(self.config) as client:
            files_api = FilesApi(client)
            res = await files_api.save_file_with_http_info(
                project_id=self.project_id,
                file_id=file_id,
                save_file_request=SaveFileRequest(extra=FileExtraSchema().dump(paratranz_file.file_model_extra)),
            )
            self._log_res(f"save_file_extra[file_id={file_id}]", res)

    @staticmethod
    def _log_res(request_name: str, res: ApiResponse[Any]) -> None:
        if 400 <= res.status_code:
            logger.error("{}: {}", request_name, res)
            return
        logger.debug("{}: {}", request_name, res)
