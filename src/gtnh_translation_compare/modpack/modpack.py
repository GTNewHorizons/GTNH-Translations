import pathlib
import zipfile
from functools import cache
from os import path
from typing import Sequence

from gtnh_translation_compare.filetypes import Filetype, FiletypeLang
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.modpack.mod import Mod
from gtnh_translation_compare.utils.file import ensure_lf


class ModPack:
    def __init__(self, pack_path: pathlib.Path):
        if len(list(pack_path.glob("mods"))) == 1:
            self.__pack_path = pack_path
        elif len(list(pack_path.glob("*/mods"))) == 1:
            self.__pack_path = pathlib.Path(path.join(list(pack_path.glob("*/mods"))[0], ".."))
        else:
            raise RuntimeError("Cannot find modpack. Maybe it's nested too much.")

    @cache
    def lang_files(self, language: Language) -> Sequence[Filetype]:
        lang_files: list[FiletypeLang] = []
        for mod_path in self.__pack_path.glob("mods/**/*.jar"):
            with mod_path.open("rb") as mod_jar:
                mod = Mod(zipfile.ZipFile(mod_jar))
                for filename, content in mod.lang_files(language).items():
                    sub_mod_id = filename.split("/")[1]
                    filename = path.join(*filename.split("/")[2:])
                    lang_files.append(FiletypeLang(f"resources/{mod.mod_name}[{sub_mod_id}]/{filename}", content))
        return lang_files
