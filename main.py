import os
import sys
from os import path
from pathlib import Path
from typing import Optional, Callable, TypeAlias

import fire  # type: ignore[import]
import requests
from dulwich import porcelain
from loguru import logger

from gtnh_translation_compare.filetypes import FiletypeLang, Language, FiletypeGTLang
from gtnh_translation_compare.issue.issue_parser import IssueBodyLines, new_issue_parser_from_env
from gtnh_translation_compare.modpack.modpack import ModPack
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import to_paratranz_file, to_translation_file, TranslationFile
from gtnh_translation_compare.utils.env import must_get_env
from gtnh_translation_compare.utils.github_action import set_output_and_print
from paratranz_client.client import AuthenticatedClient

GTNH_REPO = "https://github.com/GTNewHorizons/GT-New-Horizons-Modpack"
DEFAULT_QUESTS_LANG_EN_US_REL_PATH_IN_GTHN = "config/txloader/load/minecraft/lang/en_US.lang"
DEFAULT_QUESTS_LANG_EN_US_REL_PATH = "resources/minecraft/lang/en_US.lang"
DEFAULT_QUESTS_LANG_ZH_CN_REL_PATH = "resources/minecraft/lang/zh_CN.lang"
DEFAULT_QUESTS_JSON_REL_PATH_IN_GTNH = "config/betterquesting/DefaultQuests-us.json"
DEFAULT_QUESTS_JSON_REL_PATH = "config/betterquesting/DefaultQuests.json"
GT_LANG_EN_US_REL_PATH = "GregTech_US.lang"
GT_LANG_ZH_CN_REL_PATH = "GregTech.lang"

ParatranzFilenameFilter: TypeAlias = Callable[[str], bool]
AfterToTranslationFileCallback: TypeAlias = Callable[[TranslationFile], None]


class App:
    def __init__(self) -> None:
        self.parse_issue = ParseIssue()
        self.action = Action()


class ParseIssue:
    # region Quest Book
    @staticmethod
    def quest_book_to_paratranz() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("commit-sha", lines[2])

        new_issue_parser_from_env().parse(pf)

    @staticmethod
    def paratranz_to_quest_book() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("commit-sha", lines[2])
            set_output_and_print("branch", lines[6])

        new_issue_parser_from_env().parse(pf)

    # endregion Quest Book

    # region Lang + Zs
    @staticmethod
    def lang_and_zs_to_paratranz() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("modpack-url", lines[2])

        new_issue_parser_from_env().parse(pf)

    @staticmethod
    def paratranz_to_lang_and_zs() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("branch", lines[2])

        new_issue_parser_from_env().parse(pf)

    # endregion Lang + Zs

    # region Gt Lang
    @staticmethod
    def gt_lang_to_paratranz() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("gt-lang-url", lines[2])

        new_issue_parser_from_env().parse(pf)

    @staticmethod
    def paratranz_to_gt_lang() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("branch", lines[2])

        new_issue_parser_from_env().parse(pf)

    # endregion Gt Lang


class Action:
    def __init__(self) -> None:
        paratranz_project_id = int(must_get_env("PARATRANZ_PROJECT_ID"))
        paratranz_token = must_get_env("PARATRANZ_TOKEN")
        client = AuthenticatedClient(
            base_url="https://paratranz.cn/api",
            token=paratranz_token,
            verify_ssl=False,
            timeout=1000,
            headers={"Authorization": paratranz_token},
        )
        self.client = ClientWrapper(client, paratranz_project_id)

    @staticmethod
    def __commit(repo: str, paths: list[str], message: str, issue: object) -> None:
        porcelain.add(repo, paths)  # type: ignore[no-untyped-call]
        commit_message = message
        if issue is not None:
            commit_message += f"\n\nclosed #{issue}"
        porcelain.commit(  # type: ignore[no-untyped-call]
            repo,
            message=commit_message,
            author="MuXiu1997 <muxiu1997@gmail.com>",
        )

    @staticmethod
    def __write(filepath: str, content: str) -> None:
        os.makedirs(path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as fp:
            fp.write(content)

    @staticmethod
    def __write_translation_file(filepath: str, translation_file: TranslationFile) -> None:
        Action.__write(filepath, translation_file.content)

    def __paratranz_to_translation(
        self,
        filter_: ParatranzFilenameFilter,
        after_to_translation_file_callback: Optional[AfterToTranslationFileCallback],
        raise_when_empty: Optional[Exception],
        message: str,
        repo_path: Optional[str] = None,
        issue: Optional[str] = None,
    ) -> None:
        translation_files: list[TranslationFile] = []
        translation_filepaths: list[str] = []
        for f in self.client.all_files:
            if filter_(f.name):
                strings = self.client.get_strings(f.id)
                translation_file = to_translation_file(f, strings)
                if after_to_translation_file_callback is not None:
                    after_to_translation_file_callback(translation_file)
                translation_files.append(translation_file)

        if len(translation_files) == 0:
            if raise_when_empty is not None:
                raise raise_when_empty

        if repo_path is None:
            for translation_file in translation_files:
                print(translation_file.content)
            return

        for translation_file in translation_files:
            translation_filepath = path.abspath(path.join(repo_path, translation_file.relpath))
            translation_filepaths.append(translation_filepath)
            self.__write_translation_file(translation_filepath, translation_file)

        self.__commit(
            repo_path,
            translation_filepaths,
            message,
            issue,
        )

    # region Quest Book
    def quest_book_to_paratranz(self, commit_sha: Optional[str] = None) -> None:
        if commit_sha is None or commit_sha == "":
            commit_sha = "master"
        qb_lang_file_url = f"{GTNH_REPO}/raw/{commit_sha}/{DEFAULT_QUESTS_LANG_EN_US_REL_PATH_IN_GTHN}"
        res = requests.get(qb_lang_file_url)
        if res.status_code == 404:
            qb_lang_file_url = f"{GTNH_REPO}/raw/{commit_sha}/{DEFAULT_QUESTS_LANG_EN_US_REL_PATH}"
            res = requests.get(qb_lang_file_url)
        qb_lang_file = FiletypeLang(
            relpath=DEFAULT_QUESTS_LANG_EN_US_REL_PATH, content=res.text, language=Language.en_US
        )
        qb_paratranz_file = to_paratranz_file(qb_lang_file)
        self.client.upload_file(qb_paratranz_file)

    def paratranz_to_quest_book(
        self, repo_path: Optional[str] = None, issue: Optional[str] = None, commit_sha: Optional[str] = None
    ) -> None:
        filter_: ParatranzFilenameFilter = lambda name: name == DEFAULT_QUESTS_LANG_ZH_CN_REL_PATH + ".json"
        self.__paratranz_to_translation(
            filter_,
            None,
            ValueError("No quest book file found"),
            "[自动化] 更新 任务书",
            repo_path,
            issue,
        )
        if repo_path is None:
            return
        if commit_sha is None or commit_sha == "":
            commit_sha = "master"
        qb_json_file_url = f"{GTNH_REPO}/raw/{commit_sha}/{DEFAULT_QUESTS_JSON_REL_PATH_IN_GTNH}"
        res = requests.get(qb_json_file_url)
        qb_json_filepath = path.abspath(path.join(repo_path, DEFAULT_QUESTS_JSON_REL_PATH))
        self.__write(qb_json_filepath, res.text)
        self.__commit(repo_path, [qb_json_filepath], "[自动化] 更新 任务书 json", None)

    # endregion Quest Book

    # region Lang + Zs
    def lang_and_zs_to_paratranz(self, modpack_path: str) -> None:
        modpack = ModPack(Path(modpack_path))
        for lang_file in modpack.lang_files:
            lang_paratranz_file = to_paratranz_file(lang_file)
            self.client.upload_file(lang_paratranz_file)
        for script_file in modpack.script_files:
            script_paratranz_file = to_paratranz_file(script_file)
            self.client.upload_file(script_paratranz_file)

    def paratranz_to_lang_and_zs(self, repo_path: Optional[str] = None, issue: Optional[str] = None) -> None:
        def filter_(name: str) -> bool:
            return any(
                [
                    name.endswith(".lang" + ".json")
                    and name != DEFAULT_QUESTS_LANG_ZH_CN_REL_PATH + ".json"
                    and name != GT_LANG_ZH_CN_REL_PATH + ".json",
                    name.endswith(".zs" + ".json"),
                ]
            )

        self.__paratranz_to_translation(
            filter_,
            None,
            ValueError("No lang or zs file found"),
            "[自动化] 更新 语言文件 + 脚本",
            repo_path,
            issue,
        )

    # endregion Lang + Zs

    # region Gt Lang
    def gt_lang_to_paratranz(self, gt_lang_url: str) -> None:
        res = requests.get(gt_lang_url)
        gt_lang_file = FiletypeGTLang(relpath=GT_LANG_ZH_CN_REL_PATH, content=res.text, language=Language.en_US)
        gt_paratranz_file = to_paratranz_file(gt_lang_file)
        self.client.upload_file(gt_paratranz_file)

    def paratranz_to_gt_lang(self, repo_path: Optional[str] = None, issue: Optional[str] = None) -> None:
        filter_: ParatranzFilenameFilter = lambda name: name == GT_LANG_ZH_CN_REL_PATH + ".json"

        def after_to_translation_file_callback(translation_file: TranslationFile) -> None:
            translation_file.content = translation_file.content.replace(
                "B:UseThisFileAsLanguageFile=false", "B:UseThisFileAsLanguageFile=true"
            )

        self.__paratranz_to_translation(
            filter_,
            after_to_translation_file_callback,
            ValueError("No gt lang file found"),
            "[自动化] 更新 GT 语言文件",
            repo_path,
            issue,
        )

    # endregion Gt Lang


if __name__ == "__main__":
    if os.environ.get("GTNH_TC_DEBUG") is None:
        logger.remove(handler_id=None)
        logger.add(sys.stderr, level="INFO")
    fire.Fire(App, name="gtnh-translation-compare")
