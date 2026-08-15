import json
import pathlib
import zipfile

from gtnh_translation_compare.filetypes import Language
from gtnh_translation_compare.modpack.modpack import ModPack

MOD_NAME = "GregTech"
MOD_ID = "gregtech"
TOOLTIP_SLUG = "tooltip/space-research-module.md"


def _make_modpack(tmp_path: pathlib.Path) -> ModPack:
    mods_dir = tmp_path / "mods"
    mods_dir.mkdir(parents=True)
    with zipfile.ZipFile(mods_dir / "mod.jar", "w") as jar:
        jar.writestr("mcmod.info", json.dumps([{"modid": MOD_ID, "name": MOD_NAME}]))
        jar.writestr(f"assets/{MOD_ID}/lang/en_US.lang", "item.foo.name=Foo\n")
        jar.writestr(f"assets/{MOD_ID}/lang/ru_RU.lang", "item.foo.name=Фу\n")
        jar.writestr(f"assets/{MOD_ID}/lang/en_US/{TOOLTIP_SLUG}", "Researches stellar objects")
        jar.writestr(f"assets/{MOD_ID}/lang/ru_RU/{TOOLTIP_SLUG}", "Исследует звёздные объекты")
    return ModPack(tmp_path)


def test_lang_files_know_their_language(tmp_path: pathlib.Path) -> None:
    # A translated file has to report the en_US path it belongs to, which it can only do
    # if it was told which language it is.
    for language in (Language.en_US, Language.ru_RU):
        for lang_file in _make_modpack(tmp_path / language.name).lang_files(language):
            assert Language.en_US.value in lang_file.get_en_us_relpath()


def test_markdown_tooltip_key_is_language_independent(tmp_path: pathlib.Path) -> None:
    keys = {
        language: list(_make_modpack(tmp_path / language.name).lang_files(language)[-1].properties)
        for language in (Language.en_US, Language.ru_RU)
    }
    assert keys[Language.en_US] == keys[Language.ru_RU]
