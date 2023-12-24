import asyncio
import json
from functools import cache
from os import path
from typing import Optional, Any

from loguru import logger
from paratranz_client.api.files import get_files, create_file, save_file, update_file
from paratranz_client.api.strings import get_strings
from paratranz_client.client import Client
from paratranz_client.models import (  # type: ignore[attr-defined]
    File,
    StringItem,
    CreateFileMultipartData,
    UpdateFileMultipartData,
    SaveFileJsonBody,
    SaveFileJsonBodyExtra,
)
from paratranz_client.types import Response

from gtnh_translation_compare.paratranz.converter import ParatranzFile
from gtnh_translation_compare.paratranz.file_extra import FileExtraSchema


class ClientWrapper:
    def __init__(self, client: Client, project_id: int):
        self.client = client
        self.project_id = project_id

    @cache
    def _get_all_files(self) -> list[File]:
        res = get_files.sync_detailed(project_id=self.project_id, client=self.client)
        self._log_res("get_files.sync_detailed", res)
        return [File.from_dict(d) for d in json.loads(res.content)]

    @property
    def all_files(self) -> list[File]:
        return self._get_all_files()

    async def _get_strings_by_page(
        self, sem: asyncio.Semaphore, file_id: int, page: int, page_size: int, page_count: int
    ) -> list[StringItem]:
        async with sem:
            logger.info("get_strings:started: file_id={}, page={}, page_count={}", file_id, page, page_count)
            res = await get_strings.asyncio_detailed(
                project_id=self.project_id, file=file_id, page=page, page_size=page_size, client=self.client
            )
            self._log_res(f"get_strings.sync_detailed[file_id={file_id}, page={page}, page_count={page_count}]", res)
            logger.info("get_strings:finished: file_id={}, page={}, page_count={}", file_id, page, page_count)
        data = json.loads(res.content)
        return [StringItem.from_dict(d) for d in data["results"]]

    def get_strings(self, file_id: int) -> list[StringItem]:
        page = 1
        page_size = 1000
        logger.info("get_strings: file_id={}, page={}, page_count=?", file_id, page)
        strings: list[StringItem] = list()
        res = get_strings.sync_detailed(
            project_id=self.project_id, file=file_id, page=page, page_size=page_size, client=self.client
        )
        self._log_res(f"get_strings.sync_detailed[file_id={file_id}, page={page}, page_count=?]", res)
        data = json.loads(res.content)
        page_count = data["pageCount"]

        strings.extend([StringItem.from_dict(d) for d in data["results"]])

        sem = asyncio.Semaphore(10)

        tasks = [
            self._get_strings_by_page(sem, file_id, page, page_size, page_count) for page in range(2, page_count + 1)
        ]

        tasks_result = asyncio.get_event_loop().run_until_complete(asyncio.gather(*tasks))
        logger.info("get_strings:finished_all: file_id={}, page_count={}", file_id, page_count)
        for page_strings in tasks_result:
            strings.extend(page_strings)

        return strings

    def upload_file(self, paratranz_file: ParatranzFile) -> None:
        assert isinstance(paratranz_file.file_model.name, str)
        file_id = self._find_file_id_by_file(paratranz_file.file_model.name)

        if file_id is None:
            file_id = self._create_file(paratranz_file)
        else:
            self._update_file(file_id, paratranz_file)

        self._save_file_extra(file_id, paratranz_file)

    def _find_file_id_by_file(self, filename: str) -> Optional[int]:
        for f in self.all_files:
            if f.name == filename:
                assert isinstance(f.id, int)
                return f.id
        return None

    def _create_file(self, paratranz_file: ParatranzFile) -> int:
        assert isinstance(paratranz_file.file_model.name, str)
        res = create_file.sync_detailed(
            project_id=self.project_id,
            client=self.client,
            multipart_data=CreateFileMultipartData(
                file=paratranz_file.file, path=path.dirname(paratranz_file.file_model.name)
            ),
        )
        self._log_res("create_file.sync_detailed", res)
        assert res.parsed is not None
        assert isinstance(res.parsed.file, File)
        assert isinstance(res.parsed.file.id, int)
        file_id = res.parsed.file.id
        return file_id

    def _update_file(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        old_strings = self.get_strings(file_id)
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
        res = update_file.sync_detailed(
            project_id=self.project_id,
            file_id=file_id,
            client=self.client,
            multipart_data=UpdateFileMultipartData(file=paratranz_file.file),
        )
        self._log_res("update_file.sync_detailed", res)

    def _save_file_extra(self, file_id: int, paratranz_file: ParatranzFile) -> None:
        res = save_file.sync_detailed(
            project_id=self.project_id,
            file_id=file_id,
            client=self.client,
            json_body=SaveFileJsonBody(
                extra=SaveFileJsonBodyExtra.from_dict(FileExtraSchema().dump(paratranz_file.file_model_extra))
            ),
        )
        self._log_res("save_file.sync_detailed", res)

    @staticmethod
    def _log_res(request_name: str, res: Response[Any]) -> None:
        if 400 <= res.status_code:
            logger.error("{}: {}", request_name, res)
            return
        logger.debug("{}: {}", request_name, res)
