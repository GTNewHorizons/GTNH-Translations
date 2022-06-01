import json
import pathlib
import zipfile
from os import path
from typing import List, Dict, Sequence
from zipfile import ZipFile

import utils
from .comparable import Comparable
from .langfiletype import LangFiletype
from .scriptfiletype import ScriptFiletype


class ModPack:
    def __init__(self, pack_path: pathlib.Path):
        if len(list(pack_path.glob("resources"))) == 1:
            self.__pack_path = pack_path
        elif len(list(pack_path.glob("*/resources"))) == 1:
            self.__pack_path = pathlib.Path(path.join(list(pack_path.glob("*/resources"))[0], ".."))
        self.lang_files: Sequence[Comparable] = self.__get_lang_files()
        self.script_files: Sequence[Comparable] = self.__get_script_files()

    def __get_lang_files(self) -> Sequence[Comparable]:
        lang_files: list[LangFiletype] = []
        for mod_path in self.__pack_path.glob("mods/**/*.jar"):
            with mod_path.open("rb") as mod_jar:
                mod = Mod(zipfile.ZipFile(mod_jar))
                for filename, content in mod.lang_files.items():
                    sub_mod_id = filename.split("/")[1]
                    filename = path.join(*filename.split("/")[2:])
                    lang_files.append(LangFiletype(f"{mod.mod_name}[{sub_mod_id}]/{filename}", content))
        return lang_files

    # noinspection DuplicatedCode
    def __get_script_files(self) -> Sequence[Comparable]:
        script_files: list[ScriptFiletype] = []
        for f in self.__pack_path.glob("scripts/*.zs"):
            script_file = ScriptFiletype(f.name, utils.ensure_lf(f.read_text(encoding="utf-8", errors="ignore")))
            if 0 < len(script_file.properties):
                script_files.append(script_file)
        return script_files


class Mod:
    __jar: ZipFile
    __mod_name: str | None
    __lang_files: Dict[str, str] | None

    def __init__(self, jar: zipfile.ZipFile):
        self.__jar = jar
        self.__mod_name = None
        self.__lang_files = None

    @property
    def mod_name(self) -> str:
        if self.__mod_name is None:
            try:
                with self.__jar.open("mcmod.info", "r") as fp:
                    mod_info_json = fp.read()
                    mod_info = json.loads(mod_info_json, strict=False)
                    mod_list = mod_info
                    if isinstance(mod_info, dict):
                        mod_list = mod_list.get("modList")
                    first_mod_name = mod_list[0].get("name")
                    if len(mod_list) == 1:
                        self.__mod_name = utils.replace_illegal_characters(first_mod_name)
                    else:
                        self.__mod_name = utils.replace_illegal_characters(f"{first_mod_name}(+{len(mod_list) - 1})")
            except KeyError:
                self.__mod_name = "__no-modinfo"
        assert self.__mod_name is not None
        return self.__mod_name

    @property
    def lang_files(self) -> Dict[str, str]:
        if self.__lang_files is None:
            self.__lang_files = {}
            for f in self.__jar.namelist():
                if f.endswith("en_US.lang") and len(f.split("/")) == 4:
                    with self.__jar.open(f, mode="r") as fp:
                        self.__lang_files[f] = utils.ensure_lf(fp.read().decode("utf-8", errors="ignore"))
        return self.__lang_files
