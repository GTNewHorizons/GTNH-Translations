import re
from functools import cache
from os import path
from typing import Dict

from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property

_PATTERNS = {
    "game.setLocalization": re.compile(
        r"^(?P<full>game\.setLocalization\((?:\"en_US\", ?)?(?P<key>.+?), ?(?P<value>.+?)\);$)",
        re.M | re.S,
    ),
    "NEI.overrideName": re.compile(r"(?P<full>^NEI\.overrideName\((?P<key>.+?), ?(?P<value>.+?)\);$)", re.M | re.S),
    "addTooltip": re.compile(r"(?P<full>^(?P<key>[^/\n]+)\.addTooltip\((?P<value>.+?)\);$)", re.M | re.S),
    "displayName": re.compile(r"(?P<full>^(?P<key>[^/\n]+)\.displayName ?= ?(?P<value>.+?);$)", re.M | re.S),
}

_REPEATABLE__PATTERNS = {
    "addShiftTooltip": re.compile(
        r"(?P<full>^(?P<key>[^/\n]+)\.addShiftTooltip\((?P<value>.+?)\);)",
        re.M | re.S,
    ),
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
                key = f"script|{path.basename(self.relpath)}|{pattern_name}|{m.group('key')}"
                value = m.group("value")
                full = m.group("full")
                start = m.start()
                end = m.end()
                properties[key] = Property(key=key, value=value, full=full, start=start, end=end)
        repeatable_count = dict()
        for pattern_name, pattern in _REPEATABLE__PATTERNS.items():
            for m in pattern.finditer(content):
                key = f"script|{path.basename(self.relpath)}|{pattern_name}|{m.group('key')}"
                value = m.group("value")
                full = m.group("full")
                start = m.start()
                end = m.end()
                if key not in repeatable_count:
                    repeatable_count[key] = 0
                else:
                    repeatable_count[key] += 1
                key = f"{key}|{repeatable_count[key]}"
                properties[key] = Property(key=key, value=value, full=full, start=start, end=end)
        return properties

    def get_en_us_relpath(self) -> str:
        return self._relpath

    def get_zh_cn_relpath(self) -> str:
        return self._relpath
