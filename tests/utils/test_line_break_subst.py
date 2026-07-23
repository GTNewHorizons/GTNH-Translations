from gtnh_translation_compare.paratranz.types import File
from gtnh_translation_compare.utils.line_break_subst import line_break_subst


def test_markdown_tooltip_unescapes_literal_backslash_n() -> None:
    # ParaTranz's editor turns Enter (and Shift+Enter) into a literal "\n" for these
    # single-blob translations, no matter what the translator does, so this must
    # un-escape it back into a real line break regardless of the file's context.
    file = File(id=1, name="resources/GregTech[gregtech]/lang/ru_RU/tooltip/bec-ionode.md.json")
    translation = "Первая строка.\\nВторая строка."
    assert line_break_subst(file, None, translation) == "Первая строка.\nВторая строка."


def test_markdown_tooltip_leaves_real_newlines_alone() -> None:
    file = File(id=1, name="resources/GregTech[gregtech]/lang/ru_RU/tooltip/bec-ionode.md.json")
    translation = "Первая строка.\nВторая строка."
    assert line_break_subst(file, None, translation) == translation


def test_non_markdown_file_is_unaffected() -> None:
    file = File(id=1, name="resources/GregTech[gregtech]/lang/ru_RU.lang.json")
    translation = "test\\ntest2"
    # Not a markdown tooltip file: falls through to the existing NOOP behavior, which
    # leaves the translation untouched (only real \r?\n gets substituted, and there
    # isn't one here).
    assert line_break_subst(file, None, translation) == translation
