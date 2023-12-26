import pathlib
import zipfile
from functools import cached_property
from os import path
from typing import Sequence

from gtnh_translation_compare.filetypes import Filetype, FiletypeLang, FiletypeScript
from gtnh_translation_compare.modpack.mod import Mod
from gtnh_translation_compare.utils.file import ensure_lf


class ModPack:
    def __init__(self, pack_path: pathlib.Path):
        if len(list(pack_path.glob("mods"))) == 1:
            self.__pack_path = pack_path
        elif len(list(pack_path.glob("*/mods"))) == 1:
            self.__pack_path = pathlib.Path(path.join(list(pack_path.glob("*/mods"))[0], ".."))

    @cached_property
    def lang_files(self) -> Sequence[Filetype]:
        lang_files: list[FiletypeLang] = []
        for mod_path in self.__pack_path.glob("mods/**/*.jar"):
            with mod_path.open("rb") as mod_jar:
                mod = Mod(zipfile.ZipFile(mod_jar))
                for filename, content in mod.lang_files.items():
                    sub_mod_id = filename.split("/")[1]
                    filename = path.join(*filename.split("/")[2:])
                    lang_files.append(FiletypeLang(f"resources/{mod.mod_name}[{sub_mod_id}]/{filename}", content))
        return lang_files

    @cached_property
    def script_files(self) -> Sequence[Filetype]:
        script_files: list[FiletypeScript] = []
        for f in self.__pack_path.glob("scripts/*.zs"):
            script_file = FiletypeScript(
                f"scripts/{f.name}", ensure_lf(f.read_text(encoding="utf-8-sig", errors="ignore"))
            )
            if 0 < len(script_file.properties):
                script_files.append(script_file)
        return script_files
