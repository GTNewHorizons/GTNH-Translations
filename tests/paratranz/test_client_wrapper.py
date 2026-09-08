import asyncio
import pathlib

import httpx

from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.types import FileExtra, ParatranzFile


def _refusing_client() -> httpx.AsyncClient:
    def handler(request: httpx.Request) -> httpx.Response:
        raise AssertionError(f"unexpected request: {request.method} {request.url}")

    return httpx.AsyncClient(transport=httpx.MockTransport(handler), base_url="https://paratranz.cn/api")


def test_upload_file_skips_a_file_without_strings(tmp_path: pathlib.Path) -> None:
    # The guide pack shipped an empty page once, and ParaTranz answers a create for a file with
    # no strings without the file object, which used to end the sync for every file behind it.
    paratranz_file = ParatranzFile(
        file_name="resources/GTNH Guide Pack[gregtech]/guidenh/_ru_ru/misc/misc-index.md.json",
        file_extra=FileExtra(
            original="",
            properties={},
            en_us_relpath="resources/GTNH Guide Pack[gregtech]/guidenh/_en_us/misc/misc-index.md",
            target_relpath="resources/GTNH Guide Pack[gregtech]/guidenh/_ru_ru/misc/misc-index.md",
        ),
        string_items=[],
    )
    client = ClientWrapper(client=_refusing_client(), project_id=1, cache_dir=str(tmp_path))

    asyncio.run(client.upload_file(paratranz_file))
