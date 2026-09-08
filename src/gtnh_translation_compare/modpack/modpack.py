import pathlib
import zipfile
from functools import cache
from os import path
from typing import Sequence

from gtnh_translation_compare.filetypes import (
    Filetype,
    FiletypeGuideNhPage,
    FiletypeLang,
    FiletypeMarkdownTooltip,
)
from gtnh_translation_compare.filetypes.filetype_guidenh_page import language_folder
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.modpack.mod import Mod
from gtnh_translation_compare.utils.file import ensure_lf

# The GTNH Guide Pack is not a mod jar: the modpack's release workflow downloads the matching
# guide pack release and bundles it under this path, so the pages ride along with the modpack
# archive instead of being shipped by any mod.
GUIDE_PACK_REL_PATH = "config/guidenh/DefaultGuide.zip"
GUIDE_PACK_NAME = "GTNH Guide Pack"


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
        lang_files: list[Filetype] = []
        for mod_path in self.__pack_path.glob("mods/**/*.jar"):
            with mod_path.open("rb") as mod_jar:
                mod = Mod(zipfile.ZipFile(mod_jar))
                for filename, content in mod.lang_files(language).items():
                    sub_mod_id = filename.split("/")[1]
                    filename = path.join(*filename.split("/")[2:])
                    lang_files.append(
                        FiletypeLang(f"resources/{mod.mod_name}[{sub_mod_id}]/{filename}", content, language)
                    )
                for filename, content in mod.markdown_tooltip_files(language).items():
                    sub_mod_id = filename.split("/")[1]
                    filename = path.join(*filename.split("/")[2:])
                    lang_files.append(
                        FiletypeMarkdownTooltip(f"resources/{mod.mod_name}[{sub_mod_id}]/{filename}", content, language)
                    )
        return lang_files

    @cache
    def guide_pack_files(self, language: Language) -> Sequence[Filetype]:
        guide_pack_path = self.__pack_path / GUIDE_PACK_REL_PATH
        if not guide_pack_path.is_file():
            # Older modpack releases predate the bundled guide pack, so its absence is expected.
            return []

        files: list[Filetype] = []
        locale_folder = language_folder(language)
        # The pack writes lowercase lang file names, while the rest of the pipeline substitutes
        # the Minecraft form, so the tracked relpath has to carry "en_US.lang". GuideNH compares
        # language names case-insensitively, so the renamed file still loads in game.
        pack_lang_name = f"{language.value.lower()}.lang"
        with zipfile.ZipFile(guide_pack_path) as guide_pack:
            for filename in guide_pack.namelist():
                parts = filename.split("/")
                if len(parts) < 4 or parts[0] != "assets":
                    continue
                relpath_prefix = f"resources/{GUIDE_PACK_NAME}[{parts[1]}]"

                # assets/<namespace>/lang/<locale>.lang, holding the Ponder labels of the pack
                if len(parts) == 4 and parts[2] == "lang" and parts[3] == pack_lang_name:
                    content = ensure_lf(guide_pack.read(filename).decode("utf-8-sig", errors="ignore"))
                    files.append(FiletypeLang(f"{relpath_prefix}/lang/{language.value}.lang", content, language))
                    continue

                # assets/<namespace>/guidenh/_<locale>/<page...>.md (nested pages allowed)
                if len(parts) < 5 or parts[2] != "guidenh" or parts[3] != locale_folder:
                    continue
                if not filename.endswith(".md"):
                    continue
                content = ensure_lf(guide_pack.read(filename).decode("utf-8-sig", errors="ignore"))
                files.append(FiletypeGuideNhPage("/".join([relpath_prefix, *parts[2:]]), content, language))
        return files
