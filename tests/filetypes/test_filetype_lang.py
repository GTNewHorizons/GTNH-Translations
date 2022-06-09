from gtnh_translation_compare.filetypes.filetype_lang import FiletypeLang
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property
import pytest

EN_US_RELPATH = "test/x/en_US.lang"
EN_US_CONTENT = "\n".join(
    [
        "#test",
        "test=test",
        "",
        "test2=test2=test2",
        "test3",
    ]
)
ZH_CN_RELPATH = "test/x/zh_CN.lang"
ZH_CN_CONTENT = "\n".join(
    [
        "#test",
        "test=测试",
        "",
        "test2=测试2=测试2",
        "test3",
    ]
)


@pytest.fixture(scope="module")
def en_us_filetype_lang() -> FiletypeLang:
    return FiletypeLang(EN_US_RELPATH, EN_US_CONTENT)


@pytest.fixture(scope="module")
def zh_cn_filetype_lang() -> FiletypeLang:
    return FiletypeLang(ZH_CN_RELPATH, ZH_CN_CONTENT, Language.zh_CN)


def test__get_relpath(en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.relpath == EN_US_RELPATH
    assert zh_cn_filetype_lang.relpath == ZH_CN_RELPATH


def test__get_content(en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.content == EN_US_CONTENT
    assert zh_cn_filetype_lang.content == ZH_CN_CONTENT


def test__get_properties(en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.properties == {
        "lang+test": Property("lang+test", "test=test", 6, 15),
        "lang+test2": Property("lang+test2", "test2=test2=test2", 17, 34),
    }
    assert zh_cn_filetype_lang.properties == {
        "lang+test": Property("lang+test", "test=测试", 6, 13),
        "lang+test2": Property("lang+test2", "test2=测试2=测试2", 15, 28),
    }


def test_get_en_us_relpath(en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert zh_cn_filetype_lang.get_en_us_relpath() == EN_US_RELPATH


def test_get_zh_cn_relpath(en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.get_zh_cn_relpath() == ZH_CN_RELPATH
    assert zh_cn_filetype_lang.get_zh_cn_relpath() == ZH_CN_RELPATH
