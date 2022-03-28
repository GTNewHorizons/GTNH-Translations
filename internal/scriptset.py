import re

PATTERNS = {
    'game.setLocalization': re.compile(r'^(?P<content>game\.setLocalization\((?P<key>.+?), ?.+?\);$)', re.M | re.S),
    'NEI.overrideName': re.compile(r'(?P<content>^NEI\.overrideName\((?P<key>.+?), ?.+?\);$)', re.M | re.S),
    'addTooltip': re.compile(r'(?P<content>^(?P<key>[^/\n]+)\.addTooltip\(.+?\);$)', re.M | re.S),
    'addShiftTooltip': re.compile(
        r'(?P<content>^(?P<key>[^/\n]+)\.addShiftTooltip\(.+?\);$(?:\n^(?P=key)\.addShiftTooltip\(.+?\);$)*)',
        re.M | re.S
    ),
    'displayName': re.compile(r'(?P<content>^(?P<key>[^/\n]+)\.displayName ?= ?.+?;$)', re.M | re.S)
}


class ScriptSet:
    def __init__(self, script_files: dict[str, str]):
        self.__script_files = script_files
        self.__relpath_to_matched_map = {}
        self.__generate_maps()

    def __generate_maps(self):
        for relpath, content in self.__script_files.items():
            matched = self.__get_matched(content)
            self.__relpath_to_matched_map[relpath] = matched

    @staticmethod
    def __get_matched(content: str) -> dict[str, str]:
        matched = {}
        for pattern_name, pattern in PATTERNS.items():
            for m in pattern.finditer(content):
                key = m.group('key')
                content = m.group('content')
                matched[f'{pattern_name}+{key}'] = content
        return matched

    def get_script_file_relpath_list(self) -> list[str]:
        return list(self.__script_files.keys())

    def get_keys(self, relpath: str) -> list[str]:
        return list(self.__relpath_to_matched_map.get(relpath, {}).keys())

    def get_value(self, relpath: str, key: str, default=None) -> str:
        return self.__relpath_to_matched_map.get(relpath, {}).get(key, default)

    def get_content(self, relpath: str, default=None) -> str:
        return self.__script_files.get(relpath, default)
