# GTNH-Translation-Compare

用于 [Kiwi233/Translation-of-GTNH](https://github.com/Kiwi233/Translation-of-GTNH) 汉化包，在 [GTNH](https://github.com/GTNewHorizons/GT-New-Horizons-Modpack) 游戏版本更新时，自动化追加新版本未汉化条目，并生成 PR

Used for the Chinese localization package at [Kiwi233/Translation-of-GTNH](https://github.com/Kiwi233/Translation-of-GTNH). When the game version of [GTNH](https://github.com/GTNewHorizons/GT-New-Horizons-Modpack) is updated, it automatically appends untranslated entries of the new version and generates a PR

# To maintainers of other languages

If you need to adapt to other languages, please raise an issue or PR. You can directly use this repository instead of forking, and configure the environment variables used in [`src/gtnh_translation_compare/settings/__init__.py`](./src/gtnh_translation_compare/settings/__init__.py) in GitHub Actions.
For example, if you need to localize to 'zh_CN', you need to set the environment variable `TARGET_LANG` to 'zh_CN' in GitHub Actions.
