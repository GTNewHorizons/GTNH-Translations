from pathlib import Path

from gtnh_translation_compare.cmd.action import (
    _guidenh_page_to_txloader_path,
    _make_lang_or_markdown_filetype,
    _paratranz_name_key,
)
from gtnh_translation_compare.filetypes import FiletypeGuideNhPage, FiletypeLang, FiletypeMarkdownTooltip

GUIDE_PAGE_RELPATH = "resources/GTNH Guide Pack[gregtech]/guidenh/_ru_ru/items_blocks/singleblock_machines.md"


def test_guidenh_page_to_txloader_path() -> None:
    # GuideNH reads guide pages from the resource domain, so the bracketed display name collapses
    # to the bare domain, and the locale folder rides along untouched.
    assert _guidenh_page_to_txloader_path(GUIDE_PAGE_RELPATH) == Path(
        "config/txloader/load/gregtech/guidenh/_ru_ru/items_blocks/singleblock_machines.md"
    )


def test_make_lang_or_markdown_filetype_dispatch() -> None:
    # The daily sync feeds changed files through this dispatcher, so a guide page that falls
    # through to FiletypeLang would upload as a broken key=value parse.
    assert isinstance(_make_lang_or_markdown_filetype(GUIDE_PAGE_RELPATH, "# Machines"), FiletypeGuideNhPage)
    assert isinstance(
        _make_lang_or_markdown_filetype("resources/GregTech[gregtech]/lang/en_US/tooltip/bec-ionode.md", "Teleports"),
        FiletypeMarkdownTooltip,
    )
    assert isinstance(
        _make_lang_or_markdown_filetype("resources/GregTech[gregtech]/lang/en_US.lang", "item.foo.name=Foo"),
        FiletypeLang,
    )


def test_paratranz_name_key_ignores_renames_that_kept_the_file() -> None:
    # A leftover file has to match its successor, and the three renames seen so far changed the
    # case, swapped dashes for underscores, or dropped the "(+3)" ParaTranz once appended.
    canonical = _paratranz_name_key("resources/Angelica[angelica]/lang/ru_RU.lang.json")
    assert _paratranz_name_key("resources/Angelica(+3)[angelica]/lang/ru_RU.lang.json") == canonical
    assert _paratranz_name_key("resources/Witchery++[WitcheryExtras]/lang/ru_RU.lang.json") == _paratranz_name_key(
        "resources/Witchery++[witcheryextras]/lang/ru_RU.lang.json"
    )
    assert _paratranz_name_key(
        "resources/GTNH Guide Pack[appliedenergistics2]/guidenh/_ru_ru/ae2-mechanics/bytes-and-types.md.json"
    ) == _paratranz_name_key(
        "resources/GTNH Guide Pack[appliedenergistics2]/guidenh/_ru_ru/ae2_mechanics/bytes_and_types.md.json"
    )
    assert _paratranz_name_key("resources/Angelica[angelica]/lang/ru_RU.lang.json") != _paratranz_name_key(
        "resources/Avaritia[avaritia]/lang/ru_RU.lang.json"
    )
