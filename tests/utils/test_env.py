import os

import pytest

from gtnh_translation_compare.utils.env import must_get_env


def test_must_get_env() -> None:
    os.environ["__TEST_VALUE"] = "test"
    os.environ["__TEST_Empty"] = ""
    if "__TEST_None" in os.environ:
        del os.environ["__TEST_None"]

    assert must_get_env("__TEST_VALUE") == "test"

    with pytest.raises(Exception) as excinfo:
        must_get_env("__TEST_Empty")
    assert "Missing environment variable: __TEST_Empty" in str(excinfo.value)

    with pytest.raises(Exception) as excinfo:
        must_get_env("__TEST_None")
    assert "Missing environment variable: __TEST_None" in str(excinfo.value)
