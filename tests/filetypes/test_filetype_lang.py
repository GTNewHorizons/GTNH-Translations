from gtnh_translation_compare.filetypes import FiletypeLang, Language, Property
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
JA_JP_RELPATH = "test/x/ja_JP.lang"
JA_JP_CONTENT = "\n".join(
    [
        "#test",
        "test=テスト",
        "",
        "test2=テスト2=テスト2",
        "test3",
    ]
)
KO_KR_RELPATH = "test/x/ko_KR.lang"
KO_KR_CONTENT = "\n".join(
    [
        "#test",
        "test=테스트",
        "",
        "test2=테스트2=테스트2",
        "test3",
    ]
)


@pytest.fixture(scope="module")
def en_us_filetype_lang() -> FiletypeLang:
    return FiletypeLang(EN_US_RELPATH, EN_US_CONTENT)


@pytest.fixture(scope="module")
def zh_cn_filetype_lang() -> FiletypeLang:
    return FiletypeLang(ZH_CN_RELPATH, ZH_CN_CONTENT, Language.zh_CN)


@pytest.fixture(scope="module")
def ja_jp_filetype_lang() -> FiletypeLang:
    return FiletypeLang(JA_JP_RELPATH, JA_JP_CONTENT, Language.ja_JP)

@pytest.fixture(scope="module")
def ko_kr_filetype_lang() -> FiletypeLang:
    return FiletypeLang(KO_KR_RELPATH, KO_KR_CONTENT, Language.ko_KR)


def test__get_relpath(
    en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang, ko_kr_filetype_lang: FiletypeLang
) -> None:
    assert en_us_filetype_lang.relpath == EN_US_RELPATH
    assert zh_cn_filetype_lang.relpath == ZH_CN_RELPATH
    assert ja_jp_filetype_lang.relpath == JA_JP_RELPATH
    assert ko_kr_filetype_lang.relpath == KO_KR_RELPATH


def test__get_content(
    en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang, ko_kr_filetype_lang: FiletypeLang
) -> None:
    assert en_us_filetype_lang.content == EN_US_CONTENT
    assert zh_cn_filetype_lang.content == ZH_CN_CONTENT
    assert ja_jp_filetype_lang.content == JA_JP_CONTENT
    assert ko_kr_filetype_lang.content == KO_KR_CONTENT


def test__get_properties(
    en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang, ko_kr_filetype_lang: FiletypeLang
) -> None:
    assert en_us_filetype_lang.properties == {
        "lang|test": Property("lang|test", "test", "test=test", 11, 15),
        "lang|test2": Property("lang|test2", "test2=test2", "test2=test2=test2", 23, 34),
    }
    assert zh_cn_filetype_lang.properties == {
        "lang|test": Property("lang|test", "测试", "test=测试", 11, 13),
        "lang|test2": Property("lang|test2", "测试2=测试2", "test2=测试2=测试2", 21, 28),
    }
    assert ja_jp_filetype_lang.properties == {
        "lang|test": Property("lang|test", "テスト", "test=テスト", 11, 14),
        "lang|test2": Property("lang|test2", "テスト2=テスト2", "test2=テスト2=テスト2", 22, 31),
    }
    assert ko_kr_filetype_lang.properties == {
        "lang|test": Property("lang|test", "테스트", "test=테스트", 11, 14),
        "lang|test2": Property("lang|test2", "테스트2=테스트2", "test2=테스트2=테스트2", 22, 31),
    }


def test_get_en_us_relpath(
    en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang, ko_kr_filetype_lang: FiletypeLang
) -> None:
    assert en_us_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert zh_cn_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert ja_jp_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert ko_kr_filetype_lang.get_en_us_relpath() == EN_US_RELPATH


def test_get_zh_cn_relpath(
    en_us_filetype_lang: FiletypeLang, zh_cn_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang, ko_kr_filetype_lang: FiletypeLang
) -> None:
    assert en_us_filetype_lang.get_target_language_relpath(Language.en_US) == EN_US_RELPATH
    assert zh_cn_filetype_lang.get_target_language_relpath(Language.zh_CN) == ZH_CN_RELPATH
    assert ja_jp_filetype_lang.get_target_language_relpath(Language.ja_JP) == JA_JP_RELPATH
    assert ko_kr_filetype_lang.get_target_language_relpath(Language.ko_KR) == KO_KR_RELPATH
