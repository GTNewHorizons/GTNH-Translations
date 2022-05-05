import pathlib
from os import path
from typing import List

import utils
from .comparable import Comparable
from .langfiletype import LangFiletype
from .scriptfiletype import ScriptFiletype


class TranslationPack:
    def __init__(self, pack_path: pathlib.Path):
        self.__pack_path = pack_path
        self.lang_files: List[Comparable] = self.__get_lang_files()
        self.script_files: List[Comparable] = self.__get_script_files()

    def __get_lang_files(self) -> List[Comparable]:
        lang_files = []
        resources_path = self.__pack_path / 'resources'
        for f in resources_path.glob('**/zh_CN.lang'):
            relpath = path.relpath(f, resources_path)
            lang_files.append(LangFiletype(relpath, f.read_text(encoding='utf-8', errors='ignore')))
        return lang_files

    # noinspection DuplicatedCode
    def __get_script_files(self) -> List[Comparable]:
        script_files = []
        for f in self.__pack_path.glob('scripts/*.zs'):
            script_file = ScriptFiletype(f.name, utils.ensure_lf(f.read_text(encoding='utf-8', errors='ignore')))
            if 0 < len(script_file.properties):
                script_files.append(script_file)
        return script_files
