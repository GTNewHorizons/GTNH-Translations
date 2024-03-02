from gtnh_translation_compare.filetypes import Language, FiletypeScript, Property
import pytest

RELPATH = "test/x/test.zs"
CONTENT = "\n".join(
    [
        "// test",
        'val I18N_test_0 = "test";',
        'val I18N_test_1 = "test=test";',
        'val I18N_test_测试 = "测试";',
        'val I18N_test2=テスト2 = "テスト2";',
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
        "script|I18N_test_测试": Property(
            "script|I18N_test_测试",
            "测试",
            'val I18N_test_测试 = "测试";',
            85,
            87,
        ),
        "script|I18N_test2=テスト2": Property(
            "script|I18N_test2=テスト2",
            "テスト2",
            'val I18N_test2=テスト2 = "テスト2";',
            113,
            117,
        ),
    }


def test_get_en_us_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.get_en_us_relpath() == RELPATH


def test_get_target_language_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.get_target_language_relpath(Language.zh_CN) == RELPATH
