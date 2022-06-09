import re
from functools import cache
from os import path
from typing import Dict

from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property

_PATTERNS = {
    "game.setLocalization": re.compile(
        r"^(?P<value>game\.setLocalization\((?:\"en_US\", ?)?(?P<key>.+?), ?.+?\);$)",
        re.M | re.S,
    ),
    "NEI.overrideName": re.compile(r"(?P<value>^NEI\.overrideName\((?P<key>.+?), ?.+?\);$)", re.M | re.S),
    "addTooltip": re.compile(r"(?P<value>^(?P<key>[^/\n]+)\.addTooltip\(.+?\);$)", re.M | re.S),
    "addShiftTooltip": re.compile(
        r"(?P<value>^(?P<key>[^/\n]+)\.addShiftTooltip\(.+?\);$(?:\n^(?P=key)\.addShiftTooltip\(.+?\);$)*)",
        re.M | re.S,
    ),
    "displayName": re.compile(r"(?P<value>^(?P<key>[^/\n]+)\.displayName ?= ?.+?;$)", re.M | re.S),
}


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
        for pattern_name, pattern in _PATTERNS.items():
            for m in pattern.finditer(content):
                key = f"script+{path.basename(self.relpath)}+{pattern_name}+{m.group('key')}"
                value = m.group("value")
                start = m.start()
                end = m.end()
                properties[key] = Property(key, value, start, end)
        return properties

    def get_en_us_relpath(self) -> str:
        return self._relpath

    def get_zh_cn_relpath(self) -> str:
        return self._relpath
