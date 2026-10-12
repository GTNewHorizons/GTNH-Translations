import asyncio

import pytest

from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper


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
