import re
from typing import Dict

from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property

# Shared between mod.py's jar scanner, the daily-sync workflow's changed-file
# dispatcher, and the ParaTranz-download filter, so all three agree on what counts
# as a markdown tooltip file. Language-agnostic (matches any locale segment) since
# callers see the file under different locales depending on which side they're on.
MARKDOWN_TOOLTIP_PATH_RE = re.compile(r"/lang/[^/]+/tooltip/.*\.md$")


def is_markdown_tooltip_path(relpath: str) -> bool:
    return MARKDOWN_TOOLTIP_PATH_RE.search(relpath) is not None


def is_markdown_tooltip_paratranz_file(name: str) -> bool:
    # ParaTranz always appends ".json" to the original file's relpath.
    return is_markdown_tooltip_path(name.removesuffix(".json"))


class FiletypeMarkdownTooltip(Filetype):
    """
    A GregTech "markdown" tooltip file (`assets/<mod>/lang/<locale>/tooltip/<slug>.md`),
    loaded by `MarkdownTooltipLoader` in-game. Unlike `.lang`, there is no key=value
    structure at all: the whole file is free-form prose interleaved with `{command}`
    markup, addressed by its file path rather than by a key inside it.

    We therefore treat the entire file content as a single translatable unit, keyed by
    its own relpath. This lets translators see and reflow the whole tooltip as one
    coherent text (important for languages with different word order), and matches how
    GregTech itself treats the file: one path, one blob of text, no inner key.
    """

    def __init__(self, relpath: str, content: str, language: Language = Language.en_US):
        self._relpath = relpath
        self._content = content
        self._language = language

    def _get_relpath(self) -> str:
        return self._relpath

    def _get_content(self) -> str:
        return self._content

    def _get_properties(self, content: str) -> Dict[str, Property]:
        if content == "":
            return {}
        key = f"md-tooltip|{self._relpath}"
        return {key: Property(key=key, value=content, full=content, start=0, end=len(content))}

    def get_en_us_relpath(self) -> str:
        if self._language == Language.en_US:
            return self._relpath
        return self._relpath.replace(self._language.value, Language.en_US.value)

    def get_target_language_relpath(self, target_language: Language) -> str:
        if self._language == target_language:
            return self._relpath
        return self._relpath.replace(self._language.value, target_language.value)
