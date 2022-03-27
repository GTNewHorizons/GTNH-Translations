from os import path
from pathlib import Path

from langset import LangSet


class TranslationPack:
    def __init__(self, translation_pack_path):
        self.__translation_pack_path = Path(translation_pack_path)
        self.__resources_mod_path = Path(path.join(self.__translation_pack_path, 'resources', 'mod'))
        self.lang_set = LangSet(self.__get_lang_files())

    def __get_lang_files(self) -> dict[str, str]:
        lang_files = {}
        for _path in self.__resources_mod_path.glob('**/zh_CN.lang'):
            relpath = path.relpath(_path, self.__resources_mod_path)
            lang_files[relpath] = _path.read_text()

        return lang_files
