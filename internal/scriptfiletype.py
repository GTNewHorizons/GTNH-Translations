import re
from os import path

from .comparable import Comparable, Property

PATTERNS = {
    "game.setLocalization.en_US": re.compile(r"^(?P<value>game\.setLocalization\(\"en_US\", (?P<key>.+?), ?.+?\);$)", re.M | re.S),
    "game.setLocalization": re.compile(r"^(?P<value>game\.setLocalization\((?P<key>(?!\"en_US\").+?), ?.+?\);$)", re.M | re.S),
    "NEI.overrideName": re.compile(r"(?P<value>^NEI\.overrideName\((?P<key>.+?), ?.+?\);$)", re.M | re.S),
    "addTooltip": re.compile(r"(?P<value>^(?P<key>[^/\n]+)\.addTooltip\(.+?\);$)", re.M | re.S),
    "addShiftTooltip": re.compile(
        r"(?P<value>^(?P<key>[^/\n]+)\.addShiftTooltip\(.+?\);$(?:\n^(?P=key)\.addShiftTooltip\(.+?\);$)*)",
        re.M | re.S,
    ),
    "displayName": re.compile(r"(?P<value>^(?P<key>[^/\n]+)\.displayName ?= ?.+?;$)", re.M | re.S),
}


class ScriptFiletype(Comparable):
    def __init__(self, relpath: str, content: str):
        self.__relpath = relpath
        self.__content = content

    @property
    def relpath(self) -> str:
        return self.__relpath

    @property
    def content(self) -> str:
        return self.__content

    def get_properties(self, content: str) -> dict[str, Property]:
        properties = {}
        for pattern_name, pattern in PATTERNS.items():
            for m in pattern.finditer(content):
                key = f"script+{path.basename(self.relpath)}+{pattern_name}+{m.group('key')}"
                value = m.group("value")
                start = m.start()
                end = m.end()
                properties[key] = Property(key, value, start, end)
        return properties

