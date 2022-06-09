from gtnh_translation_compare.filetypes.filetype_gt_lang import FiletypeGTLang
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property
import pytest

EN_US_RELPATH = "GregTech_US.lang"
EN_US_CONTENT = "\n".join(
    [
        "# Configuration file",
        "",
        "enablelangfile {",
        "    B:UseThisFileAsLanguageFile=false",
        "}",
        "",
        "",
        "languagefile {",
        "    S:test=test",
        "}",
        "",
    ]
)
ZH_CN_RELPATH = "GregTech.lang"
ZH_CN_CONTENT = "\n".join(
    [
        "# Configuration file",
        "",
        "enablelangfile {",
        "    S:Language=en_US",
        "    B:UseThisFileAsLanguageFile=true",
        "}",
        "",
        "",
        "languagefile {",
        "    S:test=测试",
        "}",
        "",
    ]
)


@pytest.fixture(scope="module")
def en_us_filetype_gt_lang() -> FiletypeGTLang:
    return FiletypeGTLang(EN_US_RELPATH, EN_US_CONTENT)


@pytest.fixture(scope="module")
def zh_cn_filetype_gt_lang() -> FiletypeGTLang:
    return FiletypeGTLang(ZH_CN_RELPATH, ZH_CN_CONTENT, Language.zh_CN)


def test__get_relpath(en_us_filetype_gt_lang: FiletypeGTLang, zh_cn_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.relpath == EN_US_RELPATH
    assert zh_cn_filetype_gt_lang.relpath == ZH_CN_RELPATH


def test__get_content(en_us_filetype_gt_lang: FiletypeGTLang, zh_cn_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.content == EN_US_CONTENT
    assert zh_cn_filetype_gt_lang.content == ZH_CN_CONTENT


def test__get_properties(en_us_filetype_gt_lang: FiletypeGTLang, zh_cn_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.properties == {
        "gt+lang+    S:test": Property("gt+lang+    S:test", "    S:test=test", 96, 111),
    }
    assert zh_cn_filetype_gt_lang.properties == {
        "gt+lang+    S:test": Property("gt+lang+    S:test", "    S:test=测试", 116, 129),
    }


def test_get_en_us_relpath(en_us_filetype_gt_lang: FiletypeGTLang, zh_cn_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.get_en_us_relpath() == EN_US_RELPATH
    assert zh_cn_filetype_gt_lang.get_en_us_relpath() == EN_US_RELPATH


def test_get_zh_cn_relpath(en_us_filetype_gt_lang: FiletypeGTLang, zh_cn_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.get_zh_cn_relpath() == ZH_CN_RELPATH
    assert zh_cn_filetype_gt_lang.get_zh_cn_relpath() == ZH_CN_RELPATH
