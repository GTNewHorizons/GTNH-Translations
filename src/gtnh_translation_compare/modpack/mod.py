import json
import zipfile
from functools import cache, cached_property
from typing import TypeAlias, Dict
from gtnh_translation_compare.filetypes.language import Language

from gtnh_translation_compare.utils.file import replace_illegal_characters, ensure_lf

Filename: TypeAlias = str
Content: TypeAlias = str


class Mod:
    def __init__(self, jar: zipfile.ZipFile):
        self.__jar = jar

    @cached_property
    def mod_name(self) -> str:
        try:
            with self.__jar.open("mcmod.info", "r") as fp:
                mod_info_json = fp.read()
                mod_info = json.loads(mod_info_json, strict=False)
                mod_list = mod_info
                if isinstance(mod_info, dict):
                    mod_list = mod_list.get("modList")
                first_mod_name = mod_list[0].get("name")
                if len(mod_list) == 1:
                    return replace_illegal_characters(first_mod_name)
                else:
                    return replace_illegal_characters(f"{first_mod_name}(+{len(mod_list) - 1})")
        except KeyError:
            return "__no-modinfo"

    @cache
    def lang_files(self, language: Language) -> Dict[Filename, Content]:
        lang_files = {}
        for f in self.__jar.namelist():
            if f.endswith(f"{language.name}.lang") and len(f.split("/")) == 4:
                with self.__jar.open(f, mode="r") as fp:
                    lang_files[f] = ensure_lf(fp.read().decode("utf-8-sig", errors="ignore"))
        return lang_files
