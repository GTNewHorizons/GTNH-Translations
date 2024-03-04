# GTNH Translations

中文 / [日本語](./readmes/README_ja_JP.md) / [한국어](./readmes/README_ko_KR.md) / [Português brasileiro](./readmes/README_pt_BR.md) / [Français](./readmes/README_fr_FR.md) / [Español](./readmes/README_es_ES.md) / [Türkçe](./readmes/README_tr_TR.md) / [Deutsch](./readmes/README_de_DE.md)

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

1. Add new language entry for scripts and workflows. Searching for `es_ES` for example could help. (see commits [8f1d36a](https://github.com/GTNewHorizons/GTNH-Translations/commit/8f1d36a5e30ea39c02a19a167cf72d8643efbbc1) and [a27348c](https://github.com/GTNewHorizons/GTNH-Translations/commit/a27348c066d2de8126170e44fa17264d27aae665) for reference)
2. Add new README_xx_XX.md with a mention from README.md.
3. Add new issue template.
4. Add new label for issue.
5. Run `Sync all to ParaTranz` workflow with the new language code.
6. Run `Publish nightly lang pack` workflow with the new language code.

### How workflows work

All workflows under `./.github/workflow` directory can also be triggered manually. Go to Actions tab, select workflow, (select language) and run it. (Only project owners have permission to do this.)

- [nightly-schedule](./.github/workflows/nightly-schedule.yml) This is where the nightly schedule is triggered. 3 workflows are called sequentially, due to the way syncing to ParaTranz is written.
  - [save-nightly-modpack-history](./.github/workflows/save-nightly-modpack-history.yml) Downloads nightly modpack build from [DAXXL](https://github.com/GTNewHorizons/DreamAssemblerXXL/actions), unzips, and commits to this repository. The result of the commit will be used by the next workflow.
  - [conditional-sync-to-paratranz-parallel](./.github/workflows/conditional-sync-to-paratranz-parallel.yml) Calls the following workflow for all the languages in parallel.
    - [conditional-sync-to-paratranz](./.github/workflows/conditional-sync-to-paratranz.yml) Syncs mod lang and questbook to ParaTranz for specific language. It does not try to send all the files; Instead, it uses commit from [save-nightly-modpack-history](./.github/workflows/save-nightly-modpack-history.yml) to see which files have been actually changed and sends only them. This way the workflow can be faster. However, it has major flaw; It requires the specific commit to present before this workflow runs. Hence, nobody should (in theory) push commit between save-nightly-modpack-history and conditional-sync-to-paratranz runs, nor rerun the former before the latter runs. If something goes wrong, [sync-all-to-paratranz](./.github/workflows/sync-all-to-paratranz.yml) can force all the files to be synced. If this behavior turns out to be messy, we can stop it and switch to always uploading all the files.
  - [publish-all-nightly-lang-packs](./.github/workflows/publish-all-nightly-lang-packs.yml) Calls the following workflow for all the languages sequentially.
    - [publish-nightly-lang-pack](./.github/workflows/publish-nightly-lang-pack.yml) Pulls latest translation data from ParaTranz, commits them to this repository, and publishes as a lang pack for specific language. Anyone can download it and put it into the modpack.
- [sync-gt-lang-to-paratranz-parallel](./.github/workflows/sync-gt-lang-to-paratranz-parallel.yml) Calls the following workflow for all the languages in parallel.
  - [sync-gt-lang-to-paratranz](./.github/workflows/sync-gt-lang-to-paratranz.yml) Syncs `GregTech.lang` to ParaTranz for specific language. Due to the way GT lang is generated, it cannot be automatically uploaded as a part of nightly workflow. Contributor needs to manually upload lang file under `nightly-history` directory and run this workflow if they want to update.
- [sync-all-to-paratranz-parallel](./.github/workflows/sync-all-to-paratranz-parallel.yml) Calls the following workflow for all the languages in parallel.
  - [sync-all-to-paratranz](./.github/workflows/sync-all-to-paratranz.yml) Syncs mod lang, questbook, and GT lang to ParaTranz for specific language.

These workflows are not for running manually:

- [ensure-dependencies](./.github/actions/ensure-dependencies/action.yml) Setups Poetry environment for workflows.
- [get-project-id](./.github/actions/get-project-id/action.yml) Binds lang name (`zh_CN` for example) and ParaTranz project ID.

## How Python project works

This repository uses Python scripts for communicating with ParaTranz API.

### Run locally

Even though primary use is for GitHub workflows, you can also run it locally. Be careful, simple misoperation might ruin your entire ParaTranz project!  
In order to run it,

1. Install Python (>= 3.11.0)
2. Install Poetry
3. Set environmental variables `PARATRANZ_TOKEN`, `PARATRANZ_PROJECT_ID`, and `TARGET_LANG`
4. Run `poetry install`
5. Run `poetry run python main.py action <your favorite action>`

## Things to be done

- Import existing translations from mod jars
- Work on some mods that don't have proper localization support
- Support some config files for ParaTranz
- Include all the lang packs in the modpack releases and nightly modpack builds
- Automatically backup ParaTranz project just in case?

## Credit

MuXiu1997 for original workflows and scripts!
