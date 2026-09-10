import asyncio
import pathlib
from typing import Callable

import httpx
import pytest

from gtnh_translation_compare.cmd.action import Action
from gtnh_translation_compare.filetypes import FiletypeLang
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper, ParaTranzUploadError

LANG_FILES = [
    FiletypeLang("resources/GregTech[gregtech]/lang/en_US.lang", "item.foo.name=Foo\n"),
    FiletypeLang("resources/Witchery[witchery]/lang/en_US.lang", "item.bar.name=Bar\n"),
]


def _action(handler: Callable[[httpx.Request], httpx.Response], cache_dir: pathlib.Path) -> Action:
    action = Action()
    action.client = ClientWrapper(
        client=httpx.AsyncClient(transport=httpx.MockTransport(handler), base_url="https://paratranz.cn/api"),
        project_id=1,
        cache_dir=str(cache_dir),
    )
    action.converter.client = action.client
    return action


def _handler(create_responses: list[httpx.Response], extra_status: int = 200) -> tuple[Callable, list[str]]:
    attempted: list[str] = []

    def handle(request: httpx.Request) -> httpx.Response:
        if request.method == "GET" and request.url.path.endswith("/files"):
            return httpx.Response(200, json=[], headers={"ETag": "etag"})
        if request.method == "POST" and request.url.path.endswith("/files"):
            attempted.append(request.url.path)
            return create_responses[min(len(attempted) - 1, len(create_responses) - 1)]
        if request.method == "PUT":
            return httpx.Response(extra_status, json={})
        raise AssertionError(f"unexpected request: {request.method} {request.url}")

    return handle, attempted


def _created_file(file_id: int) -> httpx.Response:
    return httpx.Response(200, json={"file": {"id": file_id, "name": "whatever"}})


def test_a_rejected_file_lets_the_rest_upload(tmp_path: pathlib.Path) -> None:
    # A single mod lang file rejected with 400 used to abort the gather and drop every file
    # still queued behind it, which is how three language jobs lost the guide pages.
    handle, attempted = _handler([httpx.Response(400, json={"message": "invalid path"}), _created_file(2)])
    action = _action(handle, tmp_path)

    asyncio.run(action._upload_files_to_paratranz(LANG_FILES))

    assert len(attempted) == len(LANG_FILES)


def test_a_server_error_fails_the_run(tmp_path: pathlib.Path) -> None:
    # Anything that is not a per-file rejection means the sync is unreliable, so the job has to
    # fail instead of reporting a partial upload as success.
    handle, _ = _handler([httpx.Response(500, json={"message": "boom"})])
    action = _action(handle, tmp_path)

    with pytest.raises(ParaTranzUploadError):
        asyncio.run(action._upload_files_to_paratranz(LANG_FILES))


def test_an_auth_error_on_metadata_fails_the_run(tmp_path: pathlib.Path) -> None:
    # An expired token surfaces on the metadata call as well, and continuing there would send
    # hundreds of doomed requests before the batch gave up.
    handle, _ = _handler([_created_file(3)], extra_status=401)
    action = _action(handle, tmp_path)

    with pytest.raises(ParaTranzUploadError):
        asyncio.run(action._upload_files_to_paratranz(LANG_FILES))
