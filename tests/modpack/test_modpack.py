import json
import pathlib
import zipfile

from gtnh_translation_compare.filetypes import Language
from gtnh_translation_compare.modpack.modpack import ModPack

MOD_NAME = "GregTech"
MOD_ID = "gregtech"
TOOLTIP_SLUG = "tooltip/space-research-module.md"
GUIDE_PAGE_SLUG = "items_blocks/singleblock_machines.md"


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


def _add_guide_pack(pack_path: pathlib.Path) -> None:
    guide_pack_path = pack_path / "config" / "guidenh" / "DefaultGuide.zip"
    guide_pack_path.parent.mkdir(parents=True)
    with zipfile.ZipFile(guide_pack_path, "w") as guide_pack:
        guide_pack.writestr(f"assets/{MOD_ID}/guidenh/_en_us/{GUIDE_PAGE_SLUG}", "# Machines")
        guide_pack.writestr(f"assets/{MOD_ID}/guidenh/_zh_cn/{GUIDE_PAGE_SLUG}", "# 机器")
        guide_pack.writestr(f"assets/{MOD_ID}/guidenh/_en_us/assets/images/machine.png", "not markdown")
        guide_pack.writestr(f"assets/{MOD_ID}/lang/en_us.lang", "gregtech.ebf.ponder.label.overview=Overview\n")
        guide_pack.writestr(f"assets/{MOD_ID}/lang/zh_cn.lang", "gregtech.ebf.ponder.label.overview=概览\n")
        guide_pack.writestr("pack.mcmeta", "{}")


def test_guide_pack_files_are_read_per_language(tmp_path: pathlib.Path) -> None:
    modpack = _make_modpack(tmp_path)
    _add_guide_pack(tmp_path)

    en_us_files = modpack.guide_pack_files(Language.en_US)
    zh_cn_files = modpack.guide_pack_files(Language.zh_CN)

    # Non-markdown assets and other locale folders stay out of the requested language. The pack
    # names its lang files in lowercase, but the tracked relpath carries the Minecraft form.
    assert sorted(file.relpath for file in en_us_files) == [
        f"resources/GTNH Guide Pack[{MOD_ID}]/guidenh/_en_us/{GUIDE_PAGE_SLUG}",
        f"resources/GTNH Guide Pack[{MOD_ID}]/lang/en_US.lang",
    ]
    assert sorted(file.get_en_us_relpath() for file in zh_cn_files) == sorted(file.relpath for file in en_us_files)


def test_guide_pack_files_without_guide_pack(tmp_path: pathlib.Path) -> None:
    # Modpack releases older than the bundled guide pack still have to sync.
    assert _make_modpack(tmp_path).guide_pack_files(Language.en_US) == []
