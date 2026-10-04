import asyncio
import pathlib
from typing import Callable

from httpx import AsyncClient, Request, Response, MockTransport, HTTPStatusError, ReadTimeout
import pytest

from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.types import FileExtra, ParatranzFile


def _refusing_client() -> AsyncClient:
    def handler(request: Request) -> Response:
        raise AssertionError(f"unexpected request: {request.method} {request.url}")

    return AsyncClient(transport=MockTransport(handler), base_url="https://paratranz.cn/api")


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

MAX_ATTEMPTS: int = ClientWrapper._save_file_extra.retry.stop.max_attempt_number

def mock_response_200(request: Request) -> Response:
    print("[MOCK] Simulating HTTP 200")

    return Response(
        status_code=200,
        request=request,
        text="OK",
    )

def mock_response_400(request: Request) -> Response:
    print("[MOCK] Simulating HTTP 400 response")

    return Response(
        status_code=400,
        request=request,
        text="Bad Request",
    )

def mock_response_429(request: Request) -> Response:
    print("[MOCK] Simulating HTTP 429 response")

    return Response(
        status_code=429,
        request=request,
        text="Too Many Requests",
    )

def mock_response_500(request: Request) -> Response:
    print("[MOCK] Simulating HTTP 500 response ER_LOCK_DEADLOCK")

    return Response(
    status_code=500,
    request=request,
    json={
        "code": "ER_LOCK_DEADLOCK",
        "message": "update `import_history` set `uid` = 48831 "
                   "where `project` = '9461' and `id` > 640655327 - "
                   "Deadlock found when trying to get lock; "
                   "try restarting transaction",
        },
    )

def mock_response_504(request: Request) -> Response:
    print("[MOCK] Simulating HTTP 504 response")

    return Response(
        status_code=504,
        request=request,
        html="<html>\n<head><title>504 Gateway Time-out</title></head>\n<body>\n<center><h1>504 Gateway Time-out</h1></center>\n<hr><center>nginx</center>\n</body>\n</html>",
    )

def mock_response_timeout(request: Request) -> Response:
    print("[MOCK] Simulating HTTP ReadTimeout")

    raise ReadTimeout(
        "Simulated read timeout",
        request=request,
    )

def _paratranz_file() -> ParatranzFile:
    return ParatranzFile(
        file_name="a/ru/b.md.json",
        file_extra=FileExtra(
            original="",
            properties={},
            en_us_relpath="a/en/b.md",
            target_relpath="a/ru/b.md",
        ),
        string_items=[],
    )

def _call(responses: list[Callable[[Request], Response]], requests: list[Request], tmp_path: pathlib.Path) -> None:
    def handler(request: Request) -> Response:
        requests.append(request)
        return responses[min(len(requests) - 1, len(responses) - 1)](request)

    client = ClientWrapper(
        client=AsyncClient(transport=MockTransport(handler), base_url="https://paratranz.cn/api"),
        project_id=1,
        cache_dir=str(tmp_path),
    )
    asyncio.run(client._save_file_extra(1, _paratranz_file()))

@pytest.fixture(autouse=True)
def _no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    # Skip the 60s retry backoff (tenacity, up to 6 attempts) so tests only check attempts
    # and final errors. Patches asyncio.sleep and each retry-wrapped ClientWrapper method,
    # since tests hit different ones.
    real_sleep = asyncio.sleep

    async def fake_sleep(_: float) -> None:
        await real_sleep(0)

    monkeypatch.setattr(asyncio, "sleep", fake_sleep)

    for value in vars(ClientWrapper).values():
        retry = getattr(value, "retry", None)
        if retry is not None:
            monkeypatch.setattr(retry, "sleep", fake_sleep)

def test_client_wrapper_200_succeeds_without_retrying(tmp_path: pathlib.Path) -> None:
    requests: list[Request] = []
    _call([mock_response_200], requests, tmp_path)
    assert len(requests) == 1

@pytest.mark.parametrize(
    ("mock", "status"),
    [
        (mock_response_429, 429),
        (mock_response_500, 500),
        (mock_response_504, 504),
    ],
)
def test_client_wrapper_gives_up_after_max_attempts_on_retryable_status(
    mock: Callable[[Request],Response],
    status: int,
    tmp_path: pathlib.Path
) -> None:
    requests: list[Request] = []

    with pytest.raises(HTTPStatusError) as exc_info:
        _call([mock], requests, tmp_path)

    assert exc_info.value.response.status_code == status
    assert len(requests) == MAX_ATTEMPTS

def test_client_wrapper_gives_up_after_max_attempts_on_read_timeout(tmp_path: pathlib.Path) -> None:
    requests: list[Request] = []
    with pytest.raises(ReadTimeout):
        _call([mock_response_timeout], requests, tmp_path)

    assert len(requests) == MAX_ATTEMPTS

@pytest.mark.parametrize(
    "failure",
    [
        mock_response_429,
        mock_response_500,
        mock_response_504,
        mock_response_timeout,
    ],
)
def test_client_wrapper_recovers_when_a_later_attempt_succeeds(
    failure: Callable[[Request], Response],
    tmp_path: pathlib.Path
) -> None:
    requests: list[Request] = []

    _call([failure, mock_response_200], requests, tmp_path)

    assert len(requests) == 2

def test_client_wrapper_does_not_retry_non_retryable_status(tmp_path: pathlib.Path) -> None:
    requests: list[Request] = []

    with pytest.raises(HTTPStatusError):
        _call([mock_response_400], requests, tmp_path)

    assert len(requests) == 1
