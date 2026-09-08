from gtnh_translation_compare.filetypes import FiletypeGuideNhPage, Language, Property, is_guidenh_page_path
import pytest

EN_US_RELPATH = "resources/GTNH Guide Pack[gregtech]/guidenh/_en_us/items_blocks/singleblock_machines.md"
EN_US_CONTENT = "\n".join(
    [
        "---",
        "navigation:",
        "  title: Singleblock Machines",
        "---",
        "",
        "Singleblock machines consist of only one block.",
    ]
)
RU_RU_RELPATH = "resources/GTNH Guide Pack[gregtech]/guidenh/_ru_ru/items_blocks/singleblock_machines.md"
RU_RU_CONTENT = "\n".join(
    [
        "---",
        "navigation:",
        "  title: Одноблочные машины",
        "---",
        "",
        "Одноблочные машины состоят из одного блока.",
    ]
)


@pytest.fixture(scope="module")
def en_us_filetype_guidenh_page() -> FiletypeGuideNhPage:
    return FiletypeGuideNhPage(EN_US_RELPATH, EN_US_CONTENT)


@pytest.fixture(scope="module")
def ru_ru_filetype_guidenh_page() -> FiletypeGuideNhPage:
    return FiletypeGuideNhPage(RU_RU_RELPATH, RU_RU_CONTENT, Language.ru_RU)


def test__get_relpath(
    en_us_filetype_guidenh_page: FiletypeGuideNhPage,
    ru_ru_filetype_guidenh_page: FiletypeGuideNhPage,
) -> None:
    assert en_us_filetype_guidenh_page.relpath == EN_US_RELPATH
    assert ru_ru_filetype_guidenh_page.relpath == RU_RU_RELPATH


def test__get_content(
    en_us_filetype_guidenh_page: FiletypeGuideNhPage,
    ru_ru_filetype_guidenh_page: FiletypeGuideNhPage,
) -> None:
    assert en_us_filetype_guidenh_page.content == EN_US_CONTENT
    assert ru_ru_filetype_guidenh_page.content == RU_RU_CONTENT


def test__get_properties(
    en_us_filetype_guidenh_page: FiletypeGuideNhPage,
    ru_ru_filetype_guidenh_page: FiletypeGuideNhPage,
) -> None:
    # The whole page is a single translation unit, keyed by its en_US relpath so that a translated
    # page produces the same key as the English one it belongs to.
    key = f"guidenh-page|{EN_US_RELPATH}"
    assert en_us_filetype_guidenh_page.properties == {
        key: Property(key, EN_US_CONTENT, EN_US_CONTENT, 0, len(EN_US_CONTENT)),
    }
    assert ru_ru_filetype_guidenh_page.properties == {
        key: Property(key, RU_RU_CONTENT, RU_RU_CONTENT, 0, len(RU_RU_CONTENT)),
    }


def test__get_properties_empty_file() -> None:
    assert FiletypeGuideNhPage(EN_US_RELPATH, "").properties == {}


def test_get_en_us_relpath(
    en_us_filetype_guidenh_page: FiletypeGuideNhPage,
    ru_ru_filetype_guidenh_page: FiletypeGuideNhPage,
) -> None:
    assert en_us_filetype_guidenh_page.get_en_us_relpath() == EN_US_RELPATH
    assert ru_ru_filetype_guidenh_page.get_en_us_relpath() == EN_US_RELPATH


def test_get_target_relpath(
    en_us_filetype_guidenh_page: FiletypeGuideNhPage,
    ru_ru_filetype_guidenh_page: FiletypeGuideNhPage,
) -> None:
    # GuideNH names its locale folders in lowercase, so the Language value cannot be substituted as is.
    assert en_us_filetype_guidenh_page.get_target_language_relpath(Language.ru_RU) == RU_RU_RELPATH
    assert ru_ru_filetype_guidenh_page.get_target_language_relpath(Language.en_US) == EN_US_RELPATH


def test_is_guidenh_page_path() -> None:
    assert is_guidenh_page_path(EN_US_RELPATH)
    assert is_guidenh_page_path(RU_RU_RELPATH)
    assert not is_guidenh_page_path("resources/GregTech[gregtech]/lang/en_US.lang")
    assert not is_guidenh_page_path("resources/GTNH Guide Pack[gregtech]/guidenh/_en_us/index.md.json")
