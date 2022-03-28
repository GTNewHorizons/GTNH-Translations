from os import path
from pathlib import Path

from .langset import LangSet
from .scriptset import ScriptSet


class TranslationPack:
    def __init__(self, translation_pack_path):
        self.__translation_pack_path = Path(translation_pack_path)
        self.__resources_mod_path = Path(path.join(self.__translation_pack_path, 'resources', 'mod'))
        self.__scripts_path = Path(path.join(self.__translation_pack_path, 'scripts'))
        self.lang_set = LangSet(self.__get_lang_files())
        self.script_set = ScriptSet(self.__get_script_files())

    def __get_lang_files(self) -> dict[str, str]:
        lang_files = {}
        for _path in self.__resources_mod_path.glob('**/zh_CN.lang'):
            relpath = path.relpath(_path, self.__resources_mod_path)
            lang_files[relpath] = '\n'.join(_path.read_text(encoding='utf-8', errors='ignore').splitlines()) + '\n'
        return lang_files

    def __get_script_files(self) -> dict[str, str]:
        script_files = {}
        for _path in self.__scripts_path.glob('*.zs'):
            relpath = path.relpath(_path, self.__scripts_path)
            script_files[relpath] = '\n'.join(_path.read_text(encoding='utf-8', errors='ignore').splitlines()) + '\n'
        return script_files
