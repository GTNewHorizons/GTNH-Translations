from functools import cache
from typing import Dict

from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property
from gtnh_translation_compare.utils.line_iterator import line_iterator


class FiletypeLang(Filetype):
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
            if line.startswith("#"):
                continue
            split = line.split("=", 1)
            if len(split) != 2:
                continue
            key = f"lang+{split[0]}"
            value = line
            properties[key] = Property(key, value, start, end)
        return properties

    def get_en_us_relpath(self) -> str:
        if self._language == Language.en_US:
            return self._relpath
        return self._relpath.replace("zh_CN", "en_US")

    def get_zh_cn_relpath(self) -> str:
        if self._language == Language.zh_CN:
            return self._relpath
        return self._relpath.replace("en_US", "zh_CN")
