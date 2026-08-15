from gtnh_translation_compare.filetypes import FiletypeMarkdownTooltip, Language, Property, is_markdown_tooltip_path
import pytest

EN_US_RELPATH = "resources/GregTech[gregtech]/lang/en_US/tooltip/bec-ionode.md"
EN_US_CONTENT = "\n".join(
    [
        "Teleports items into and out of the {gold:{item:gregtech:gt.blockmachines:15756}}.",
        "Recipe logic is the same as all other multiblocks.",
    ]
)
RU_RU_RELPATH = "resources/GregTech[gregtech]/lang/ru_RU/tooltip/bec-ionode.md"
RU_RU_CONTENT = "\n".join(
    [
        "Телепортирует предметы в {gold:{item:gregtech:gt.blockmachines:15756}} и обратно.",
        "Логика рецептов такая же, как и у всех других мультиблоков.",
    ]
)


@pytest.fixture(scope="module")
def en_us_filetype_markdown_tooltip() -> FiletypeMarkdownTooltip:
    return FiletypeMarkdownTooltip(EN_US_RELPATH, EN_US_CONTENT)


@pytest.fixture(scope="module")
def ru_ru_filetype_markdown_tooltip() -> FiletypeMarkdownTooltip:
    return FiletypeMarkdownTooltip(RU_RU_RELPATH, RU_RU_CONTENT, Language.ru_RU)


def test__get_relpath(
    en_us_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
    ru_ru_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
) -> None:
    assert en_us_filetype_markdown_tooltip.relpath == EN_US_RELPATH
    assert ru_ru_filetype_markdown_tooltip.relpath == RU_RU_RELPATH


def test__get_content(
    en_us_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
    ru_ru_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
) -> None:
    assert en_us_filetype_markdown_tooltip.content == EN_US_CONTENT
    assert ru_ru_filetype_markdown_tooltip.content == RU_RU_CONTENT


def test__get_properties(
    en_us_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
    ru_ru_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
) -> None:
    # The whole file is a single translation unit, keyed by its en_US relpath so that a translated
    # file produces the same key as the English one it belongs to.
    key = f"md-tooltip|{EN_US_RELPATH}"
    assert en_us_filetype_markdown_tooltip.properties == {
        key: Property(key, EN_US_CONTENT, EN_US_CONTENT, 0, len(EN_US_CONTENT)),
    }
    assert ru_ru_filetype_markdown_tooltip.properties == {
        key: Property(key, RU_RU_CONTENT, RU_RU_CONTENT, 0, len(RU_RU_CONTENT)),
    }


def test__get_properties_empty_file() -> None:
    assert FiletypeMarkdownTooltip(EN_US_RELPATH, "").properties == {}


def test_get_en_us_relpath(
    en_us_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
    ru_ru_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
) -> None:
    assert en_us_filetype_markdown_tooltip.get_en_us_relpath() == EN_US_RELPATH
    assert ru_ru_filetype_markdown_tooltip.get_en_us_relpath() == EN_US_RELPATH


def test_get_target_relpath(
    en_us_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
    ru_ru_filetype_markdown_tooltip: FiletypeMarkdownTooltip,
) -> None:
    assert en_us_filetype_markdown_tooltip.get_target_language_relpath(Language.ru_RU) == RU_RU_RELPATH
    assert ru_ru_filetype_markdown_tooltip.get_target_language_relpath(Language.en_US) == EN_US_RELPATH


def test_is_markdown_tooltip_path() -> None:
    assert is_markdown_tooltip_path(EN_US_RELPATH)
    assert is_markdown_tooltip_path(RU_RU_RELPATH)
    assert not is_markdown_tooltip_path("resources/GregTech[gregtech]/lang/en_US.lang")
    assert not is_markdown_tooltip_path("resources/GregTech[gregtech]/lang/en_US/tooltip/bec-ionode.md.json")
