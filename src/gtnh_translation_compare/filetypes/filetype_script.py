import re
from functools import cache
from typing import Dict

from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property
from gtnh_translation_compare.utils.line_iterator import line_iterator

_PATTERN = re.compile(r"^(?P<full>val (?P<key>I18N.*?) ?= ?\"(?P<value>.+?)\";)$")


class FiletypeScript(Filetype):
    def __init__(self, relpath: str, content: str, language: Language = Language.en_US):
        self._relpath = relpath
        self._content = content
        self._language = language

    def _get_relpath(self) -> str:
        return self._relpath

    def _get_content(self) -> str:
        return self._content

    @cache
    def _get_properties(self, content: str) -> Dict[str, Property]:
        properties: Dict[str, Property] = {}
        for _, line, start, end in line_iterator(content):
            if not line.startswith("val I18N"):
                continue
            match = _PATTERN.search(line)
            assert match is not None
            key = match.group("key")
            s_key = f"script|{key}"
            value = match.group("value")
            full = match.group("full")
            properties[s_key] = Property(
                key=s_key,
                value=value,
                full=full,
                start=start + match.start("value"),
                end=start + match.end("value"),
            )
        return properties

    def get_en_us_relpath(self) -> str:
        return self._relpath

    def get_target_language_relpath(self, target_language: Language) -> str:
        return self._relpath
