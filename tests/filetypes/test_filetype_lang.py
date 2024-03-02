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
PT_BR_RELPATH = "test/x/pt_BR.lang"
PT_BR_CONTENT = "\n".join(
    [
        "#test",
        "test=teste",
        "",
        "test2=teste2=teste2",
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


@pytest.fixture(scope="module")
def pt_br_filetype_lang() -> FiletypeLang:
    return FiletypeLang(PT_BR_RELPATH, PT_BR_CONTENT, Language.pt_BR)


def test__get_relpath(
    en_us_filetype_lang: FiletypeLang,
    zh_cn_filetype_lang: FiletypeLang,
    ja_jp_filetype_lang: FiletypeLang,
    ko_kr_filetype_lang: FiletypeLang,
    pt_br_filetype_lang: FiletypeLang,
) -> None:
    assert en_us_filetype_lang.relpath == EN_US_RELPATH
    assert zh_cn_filetype_lang.relpath == ZH_CN_RELPATH
    assert ja_jp_filetype_lang.relpath == JA_JP_RELPATH
    assert ko_kr_filetype_lang.relpath == KO_KR_RELPATH
    assert pt_br_filetype_lang.relpath == PT_BR_RELPATH


def test__get_content(
    en_us_filetype_lang: FiletypeLang,
    zh_cn_filetype_lang: FiletypeLang,
    ja_jp_filetype_lang: FiletypeLang,
    ko_kr_filetype_lang: FiletypeLang,
    pt_br_filetype_lang: FiletypeLang,
) -> None:
    assert en_us_filetype_lang.content == EN_US_CONTENT
    assert zh_cn_filetype_lang.content == ZH_CN_CONTENT
    assert ja_jp_filetype_lang.content == JA_JP_CONTENT
    assert ko_kr_filetype_lang.content == KO_KR_CONTENT
    assert pt_br_filetype_lang.content == PT_BR_CONTENT


def test__get_properties(
    en_us_filetype_lang: FiletypeLang,
    zh_cn_filetype_lang: FiletypeLang,
    ja_jp_filetype_lang: FiletypeLang,
    ko_kr_filetype_lang: FiletypeLang,
    pt_br_filetype_lang: FiletypeLang,
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
    assert pt_br_filetype_lang.properties == {
        "lang|test": Property("lang|test", "teste", "test=teste", 11, 16),
        "lang|test2": Property("lang|test2", "teste2=teste2", "test2=teste2=teste2", 24, 37),
    }


def test_get_en_us_relpath(
    en_us_filetype_lang: FiletypeLang,
    zh_cn_filetype_lang: FiletypeLang,
    ja_jp_filetype_lang: FiletypeLang,
    ko_kr_filetype_lang: FiletypeLang,
    pt_br_filetype_lang: FiletypeLang,
) -> None:
    assert en_us_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert zh_cn_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert ja_jp_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert ko_kr_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert pt_br_filetype_lang.get_en_us_relpath() == EN_US_RELPATH


def test_get_target_relpath(
    en_us_filetype_lang: FiletypeLang,
    zh_cn_filetype_lang: FiletypeLang,
    ja_jp_filetype_lang: FiletypeLang,
    ko_kr_filetype_lang: FiletypeLang,
    pt_br_filetype_lang: FiletypeLang,
) -> None:
    # en_us to target
    assert en_us_filetype_lang.get_target_language_relpath(Language.zh_CN) == ZH_CN_RELPATH

    # non en_us to target
    assert zh_cn_filetype_lang.get_target_language_relpath(Language.ja_JP) == JA_JP_RELPATH
    assert ja_jp_filetype_lang.get_target_language_relpath(Language.zh_CN) == ZH_CN_RELPATH
    assert ko_kr_filetype_lang.get_target_language_relpath(Language.zh_CN) == ZH_CN_RELPATH
    assert pt_br_filetype_lang.get_target_language_relpath(Language.zh_CN) == ZH_CN_RELPATH
