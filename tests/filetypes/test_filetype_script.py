from gtnh_translation_compare.filetypes.filetype_script import FiletypeScript
from gtnh_translation_compare.filetypes.property import Property
import pytest

RELPATH = "test/x/test.zs"
CONTENT = "\n".join(
    [
        "// test",
        'val I18N_test_0 = "test";',
        'val I18N_test_1 = "test=test";',
    ]
)


@pytest.fixture(scope="module")
def filetype_script() -> FiletypeScript:
    return FiletypeScript(RELPATH, CONTENT)


def test__get_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.relpath == RELPATH


def test__get_content(filetype_script: FiletypeScript) -> None:
    assert filetype_script.content == CONTENT


def test__get_properties(filetype_script: FiletypeScript) -> None:
    assert filetype_script.properties == {
        "script|I18N_test_0": Property(
            "script|I18N_test_0",
            "test",
            'val I18N_test_0 = "test";',
            27,
            31,
        ),
        "script|I18N_test_1": Property(
            "script|I18N_test_1",
            "test=test",
            'val I18N_test_1 = "test=test";',
            53,
            62,
        ),
    }


def test_get_en_us_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.get_en_us_relpath() == RELPATH


def test_get_zh_cn_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.get_zh_cn_relpath() == RELPATH
