from pathlib import Path

from gtnh_translation_compare.cmd.action import (
    _guidenh_page_to_txloader_path,
    _make_lang_or_markdown_filetype,
    _orphan_summary,
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


def test_orphan_summary_groups_by_successor_and_translations() -> None:
    # The groups decide what a maintainer may delete, so an orphan with translations must never
    # land in a "safe to delete" table.
    summary = _orphan_summary([
        ("b.md.json", 0, "b_new.md.json"),
        ("a.md.json", 2, "a_new.md.json"),
        ("c.md.json", 0, None),
        ("d.md.json", 1, None),
    ])
    sections = summary.split("### ")[1:]
    assert summary.startswith("## Orphaned ParaTranz files: 4")
    assert [s.split(" (")[0] for s in sections] == [
        "Successor exists, no translations: safe to delete",
        "Successor exists, has translations: move them to the successor first",
        "No successor, no translations: safe to delete",
        "No successor, has translations: delete only on purpose",
    ]
    assert "`b.md.json` | 0 | `b_new.md.json`" in sections[0]
    assert "`a.md.json` | 2 | `a_new.md.json`" in sections[1]
    assert "`c.md.json` | 0 |  |" in sections[2]
    assert "`d.md.json` | 1 |  |" in sections[3]
    assert "### " not in _orphan_summary([("c.md.json", 0, None)]).split("safe to delete")[1]
