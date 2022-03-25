from os import path
from pathlib import Path

from langset import LangSet


class TranslationPack(LangSet):
    def __init__(self, translation_pack_path):
        super().__init__()
        self.__translation_pack_path = Path(translation_pack_path)
        self.__resources_mod_path = Path(path.join(self.__translation_pack_path, 'resources', 'mod'))

        self.__lang_map = None

    @property
    def lang_map(self):
        if self.__lang_map is None:
            self.__lang_map = {}
            for p in self.__resources_mod_path.glob('**/zh_CN.lang'):
                file_name = path.relpath(p, self.__resources_mod_path)
                self.__lang_map[file_name] = p.read_text()
        return self.__lang_map
