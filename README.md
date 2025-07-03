# GTNH Translations

[中文](./readmes/README_zh_CN.md) / [日本語](./readmes/README_ja_JP.md) / [한국어](./readmes/README_ko_KR.md) / [Português brasileiro](./readmes/README_pt_BR.md) / [Français](./readmes/README_fr_FR.md) / [Español](./readmes/README_es_ES.md) / [Türkçe](./readmes/README_tr_TR.md) / [Deutsch](./readmes/README_de_DE.md) / [Polski](./readmes/README_pl_PL.md) /[Русский язык](./readmes/README_ru_RU.md)

This is a repository managing all the translations for GTNH.

<!-- Contents below don't need to be translated! -->

## For translators

### Why?

We decided to manage all the translations under this repository for these reasons:

- Each language has one central team so that everyone can collaborate.
- We can share workflows to manage all the translations, information on changes made to mods, etc.
- Managing translations on external website is by far convenient than on GitHub.

### I want to make contribution to existing language

Each project has its own ParaTranz project. You can join there with your GitHub account.

- [zh_CN](https://paratranz.cn/projects/4964)
- [ja_JP](https://paratranz.cn/projects/8922)
- [ko_KR](https://paratranz.cn/projects/9359)
- [pt_BR](https://paratranz.cn/projects/9385)
- [fr_FR](https://paratranz.cn/projects/9461)
- [es_ES](https://paratranz.cn/projects/9508)
- [tr_TR](https://paratranz.cn/projects/9509)
- [de_DE](https://paratranz.cn/projects/9510)
- [pl_PL](https://paratranz.cn/projects/9513)
- [ru_RU](https://paratranz.cn/projects/9929)

### I want to make contribution to language that is not listed here

If you have 3 or more translators for the language, please contact boubou_19.

## For translation managers / GTNH members

### Policies

1. All the work about translations will go through ParaTranz, and exported to GTNH-Translations repository via automated commits thanks to ParaTranz API.
2. To have an lang file on the repo, we need to have at least 3 translators for the language, so the review can be less biased.
3. Same goes for the language threads in #translation-dev channel on Discord.
4. Each translating community must have a translator in chief, which will be the lead on the ParaTranz project. He/she has the final word on whatever issue(s) there might be.
5. To avoid a ParaTranz project to ever go static because the lead became unreachable, each project must add a special GTNH account so the GTNH Team can always take over on the project, to nominate another lead, etc.
6. Any issue within the pack about translation, being it either wrong translation, missing translation, or localization requests, must go to GTNH-Translations repository.

### When adding new language

1. Make ParaTranz project, and contact boubou to give `GregtechNewHorizons` Manager role.
2. Add new language entry for scripts and workflows. Searching for `pl_PL` for example could help. (see commit [ea67c0e](https://github.com/GTNewHorizons/GTNH-Translations/commit/ea67c0ecd7b1a5b81a2b04082d0930ae8dcfffff) for reference)
3. Add a pair of language name and ParaTranz project ID to [paratranz-projects.json](./paratranz-projects.json).
4. Add new README_xx_XX.md with a mention from README.md.
5. Add new issue template.
6. Add new label for issue.
7. Run `Sync all to ParaTranz` workflow with the new language code.
8. Run `Publish daily lang pack` workflow with the new language code.
9. (Optional) Run `Upload mod jar translations` workflow to import existing translations in mod jars. You can skip this if you don't want. Or you can run Python script locally to choose which mod to upload, see [List of available actions](#list-of-available-actions).

### How workflows work

All workflows under `./.github/workflow` directory can also be triggered manually. Go to Actions tab, select workflow, (select language) and run it. (Only project owners have permission to do this.)

- [daily-schedule](./.github/workflows/daily-schedule.yml) This is where the daily schedule is triggered. 3 workflows are called sequentially, due to the way syncing to ParaTranz is written.
  - [save-daily-modpack-history](./.github/workflows/save-daily-modpack-history.yml) Downloads daily modpack build from [DAXXL](https://github.com/GTNewHorizons/DreamAssemblerXXL/actions), unzips, and commits to this repository. The result of the commit will be used by the next workflow.
  - [conditional-sync-to-paratranz-parallel](./.github/workflows/conditional-sync-to-paratranz-parallel.yml) Calls the following workflow for all the languages in parallel.
    - [conditional-sync-to-paratranz](./.github/workflows/conditional-sync-to-paratranz.yml) Syncs mod lang and questbook to ParaTranz for specific language. It does not try to send all the files; Instead, it uses commit from [save-daily-modpack-history](./.github/workflows/save-daily-modpack-history.yml) to see which files have been actually changed and sends only them. This way the workflow can be faster. However, it has major flaw; It requires the specific commit to present before this workflow runs. Hence, nobody should (in theory) push commit between save-daily-modpack-history and conditional-sync-to-paratranz runs, nor rerun the former before the latter runs. If something goes wrong, [sync-all-to-paratranz](./.github/workflows/sync-all-to-paratranz.yml) can force all the files to be synced. If this behavior turns out to be messy, we can stop it and switch to always uploading all the files.
  - [publish-all-daily-lang-packs](./.github/workflows/publish-all-daily-lang-packs.yml) Calls the following workflow for all the languages sequentially.
    - [publish-daily-lang-pack](./.github/workflows/publish-daily-lang-pack.yml) Pulls latest translation data from ParaTranz, commits them to this repository, and publishes as a lang pack for specific language. Anyone can download it and put it into the modpack.
- [sync-gt-lang-to-paratranz-all-langs](./.github/workflows/sync-gt-lang-to-paratranz-all-langs.yml) Calls the following workflow for all the languages sequentially.
  - [sync-gt-lang-to-paratranz](./.github/workflows/sync-gt-lang-to-paratranz.yml) Syncs `GregTech.lang` to ParaTranz for specific language. Due to the way GT lang is generated, it cannot be automatically uploaded as a part of daily workflow. Contributor needs to manually upload lang file under `daily-history` directory and run this workflow if they want to update.
- [sync-all-to-paratranz-all-langs](./.github/workflows/sync-all-to-paratranz-all-langs.yml) Calls the following workflow for all the languages sequentially.
  - [sync-all-to-paratranz](./.github/workflows/sync-all-to-paratranz.yml) Syncs mod lang, questbook, and GT lang to ParaTranz for specific language.
- [upload-jar-translations](./.github/workflows/upload-jar-translations.yml) Uploads existing translations in mod jars to ParaTranz for specific language. If you want to choose which mod to upload, you can run it locally. Refer to [List of available actions](#list-of-available-actions).

These workflows are not for running manually:

- [ensure-dependencies](./.github/actions/ensure-dependencies/action.yml) Setups Poetry environment for workflows.
- [get-project-id](./.github/actions/get-project-id/action.yml) Binds lang name (`zh_CN` for example) and ParaTranz project ID.

## How Python script works

This repository uses Python scripts for communicating with ParaTranz API.

### Run locally

Even though primary use is for GitHub workflows, you can also run it locally. Be careful, simple misoperation might ruin your entire ParaTranz project!  
In order to run it,

1. Install Python (>= 3.11.0)
2. Install Poetry
3. Set environmental variables `PARATRANZ_TOKEN`, `PARATRANZ_PROJECT_ID`, and `TARGET_LANG`
4. Run `poetry install`
5. Run `poetry run python main.py action <your favorite action>`

### List of available actions

ParaTranz -> Local

- sync-from-paratranz

Local/Daily -> ParaTranz

- gt-lang-to-paratranz
- save-daily-modpack-history
- conditional-sync-to-paratranz
- sync-all-to-paratranz

Translations in mod jars -> ParaTranz

- list-jar-translations
  - Prints all the jar names that contain lang file for your language. _This does not upload files._
    - `--modpack_path` Path to the modpack. It needs to be unzipped.
- view-jar-translations
  - Prints the content of translations in mod jars. You can view one by one. _This does not upload files._
    - `--modpack_path` Path to the modpack. It needs to be unzipped.
- upload-jar-translations
  - Uploads existing translations in mod jars to ParaTranz.
    - `--modpack_path` Path to the modpack. It needs to be unzipped.
    - (Optional)`--interactive` True by default. It prints the contents of the translation and asks you whether to adopt it or not, for each jar. Setting False means it uploads all the translations without asking you, which is the same behavior as `upload-jar-translations` workflow.

### Other available Python scripts

- [future_mc_lang_diff](./.github/scripts/future_mc_lang_diff.py)
  - Fetches vanilla translations from future version and compares to 1.7.10. You can put the resulting lang file to `config/txloader/load/lang` folder to include in the pack.

## Things to be done

- Fix entries with (+n) notation
- Add support for IC2
- Support ____gtnhoverridenames [#12](https://github.com/GTNewHorizons/GTNH-Translations/issues/12)
- Support non-standard config files for ParaTranz [#20](https://github.com/GTNewHorizons/GTNH-Translations/issues/20)
- Support docs for OpenComputers and Computronics [#17](https://github.com/GTNewHorizons/GTNH-Translations/issues/17)
- Figure out what to do with BLS translation
- Allow pulling only reviewed strings [#19](https://github.com/GTNewHorizons/GTNH-Translations/issues/19)
- Include Better Line Break in the pack
- Include Untranslated Items
- pt_BR to pt_PT conversion script
- Refine the way conditional sync works
- Eliminate GregTech.lang
- Automatically backup ParaTranz project just in case?

## Credit

MuXiu1997 for original workflows and scripts!
