import json
import re
import zipfile
from os import path

import utils

from .langset import LangSet
from .scriptset import ScriptSet


class ModPack:
    def __init__(self, zif_file: zipfile.ZipFile):
        self.__zif_file = zif_file
        self.__mod_name_list = self.__get_mod_name_list()
        self.lang_set = LangSet(self.__get_lang_files())
        self.script_set = ScriptSet(self.__get_script_files())

    def __get_mod_name_list(self) -> list[str]:
        return [f for f in self.__zif_file.namelist() if re.match(r'^mods/.*\.jar$', f)]

    def __get_lang_files(self) -> dict[str, str]:
        lang_files = {}
        for mod_name in self.__mod_name_list:
            with self.__zif_file.open(mod_name) as mod_jar:
                mod = Mod(zipfile.ZipFile(mod_jar))
                for filename, content in mod.lang_files.items():
                    lang_files[f'{mod.mod_name}/{filename}'] = content
        return lang_files

    def __get_script_files(self) -> dict[str, str]:
        script_files = {}
        for f in self.__zif_file.namelist():
            if re.match(r'^scripts/.*\.zs$', f):
                with self.__zif_file.open(f) as script_file:
                    script_files[path.basename(f)] = '\n'.join(
                        script_file.read().decode('utf-8', errors='ignore').splitlines()
                    ) + '\n'
        return script_files


class Mod:
    def __init__(self, jar: zipfile.ZipFile):
        self.__jar = jar
        self.__mod_name = None
        self.__lang_files = None

    @property
    def mod_name(self) -> str:
        if self.__mod_name is None:
            try:
                with self.__jar.open('mcmod.info', 'r') as fp:
                    mod_info_json = fp.read()
                    mod_info = json.loads(mod_info_json, strict=False)
                    mod_list = mod_info
                    if isinstance(mod_info, dict):
                        mod_list = mod_list.get('modList')
                    first_mod_name = mod_list[0].get('name')
                    if len(mod_list) == 1:
                        self.__mod_name = utils.replace_illegal_characters(first_mod_name)
                    else:
                        self.__mod_name = utils.replace_illegal_characters(f'{first_mod_name}(+{len(mod_list) - 1})')
            except KeyError:
                self.__mod_name = '__no-modinfo'
        return self.__mod_name

    @property
    def lang_files(self) -> dict[str, str]:
        if self.__lang_files is None:
            self.__lang_files = {}
            for f in self.__jar.namelist():
                if f.endswith('en_US.lang'):
                    with self.__jar.open(f, mode='r') as fp:
                        self.__lang_files[f] = '\n'.join(fp.read().decode('utf-8', errors='ignore').splitlines()) + '\n'
        return self.__lang_files
