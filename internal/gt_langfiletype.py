import re

from .comparable import Comparable

LANG_LINE_PATTERN = re.compile(r'(?P<value>^(?P<key>(?!(#|//)).*?)=.*$)', re.M)


class GTLangFiletype(Comparable):
    def __init__(self, relpath: str, content: str):
        self.__relpath = relpath
        self.__content = content

    @property
    def relpath(self) -> str:
        return self.__relpath

    @property
    def content(self) -> str:
        return self.__content

    def get_properties(self, content: str) -> dict[str, str]:
        properties = {}
        for m in LANG_LINE_PATTERN.finditer(content):
            key = m.group('key')
            value = m.group('value')
            properties[f'gt+lang+{key}'] = value
        return properties

    def convert_relpath(self, relpath: str) -> str:
        return relpath.replace('GregTech_US', 'GregTech')
