# GTNH Translations

中文 / [日本語](./README_ja_JP.md) / [한국어](./README_ko_KR.md) / Português brasileiro / Français

This is a repository managing all the translations for GTNH.

<!-- Contents below don't need to be translated! -->

## For translators

### Why?

We dicided to manage all the translations under this repository for these reasons:

- Each language has one central team so that everyone can collaborate.
- We can share workflows to manage all the translations, information on changes made to mods, etc.
- Managing translations on external site is by far convenient than on GitHub.

### I want to make contribution to existing language

Each project has its own ParaTranz project. You can join there with your GitHub account.

### I want to make contribution to language that is not listed

If you have 3 or more translators for the language, please contact boubou_19.

## For translation managers / GTNH members

### Policies

1. All the work about translations will go through Paratranz, and exported to GTNH-Translations via automated commits thanks to Paratranz API.
2. To have an lang file on the repo, we need to have at least 3 translators for the language, so the review can be less biased. Same goes for the language threads in #translation-dev channel on Discord.
3. Each translating community must have a translator in chief, which will be the lead on the Paratranz project. He has the final word on whatever issue(s) there might be.
4. To avoid a paratranz project to ever go static because the lead became unreachable, each project must add a special GTNH account so the GTNH Team can always take over on the project, to nominate another lead, etc.
5. Any issue within the pack about translation, being it either wrong translation, missing translation, or localisation requests, must go on the GTNH-Translations repository.

### When adding new language

1. Add new language entry for scripts and workflows. Searching for `fr_FR` for example could help.
2. Add new README_xx_XX.md with a mention from README.md.
3. Add new issue template.
4. Add new label for issue.

### How workflows work

All the workflows can be triggered manually.

- [nightly-schedule.yml](./.github/workflows/nightly-schedule.yml)
  - This is where the nightly schedule is triggered.
(to be written)

## Credit

MuXiu1997 for original workflows and scripts!
