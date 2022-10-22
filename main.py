from os import path
from typing import Optional

import fire  # type: ignore[import]
import requests
from dulwich import porcelain
from gtnh_translation_compare.filetypes import FiletypeLang, Language
from gtnh_translation_compare.issue.issue_parser import IssueBodyLines, new_issue_parser_from_env
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import to_paratranz_file, to_translation_file, TranslationFile
from gtnh_translation_compare.utils.env import must_get_env
from gtnh_translation_compare.utils.github_action import set_output_and_print
from paratranz_client.client import AuthenticatedClient

GTNH_REPO = "https://github.com/GTNewHorizons/GT-New-Horizons-Modpack"
DEFAULT_QUESTS_LANG_EN_US_REL_PATH = "resources/minecraft/lang/en_US.lang"
DEFAULT_QUESTS_LANG_ZH_CN_REL_PATH = "resources/minecraft/lang/zh_CN.lang"


class App:
    def __init__(self) -> None:
        self.parse_issue = ParseIssue()
        self.action = Action()


class ParseIssue:
    @staticmethod
    def quest_book_to_paratranz() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("commit-sha", lines[2])

        new_issue_parser_from_env().parse(pf)

    @staticmethod
    def paratranz_to_quest_book() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("branch", lines[2])

        new_issue_parser_from_env().parse(pf)


class Action:
    def __init__(self) -> None:
        paratranz_project_id = int(must_get_env("PARATRANZ_PROJECT_ID"))
        paratranz_token = must_get_env("PARATRANZ_TOKEN")
        client = AuthenticatedClient(
            base_url="https://paratranz.cn/api",
            token=paratranz_token,
            verify_ssl=True,
            timeout=1000,
            headers={"Authorization": paratranz_token},
        )
        self.client = ClientWrapper(client, paratranz_project_id)

    def quest_book_to_paratranz(self, commit_sha: Optional[str] = None) -> None:
        if commit_sha is None or commit_sha == "":
            commit_sha = "master"
        qb_json_file_url = f"{GTNH_REPO}/raw/{commit_sha}/{DEFAULT_QUESTS_LANG_EN_US_REL_PATH}"
        res = requests.get(qb_json_file_url)
        qb_lang_file = FiletypeLang(
            relpath=DEFAULT_QUESTS_LANG_EN_US_REL_PATH, content=res.text, language=Language.en_US
        )
        qb_paratranz_file = to_paratranz_file(qb_lang_file)
        self.client.upload_file(qb_paratranz_file)

    def paratranz_to_quest_book(self, repo_path: Optional[str] = None, issue: Optional[str] = None) -> None:
        qb_translation_file: TranslationFile
        for f in self.client.all_files:
            if f.name == DEFAULT_QUESTS_LANG_ZH_CN_REL_PATH + ".json":
                strings = self.client.get_strings(f.id)
                qb_translation_file = to_translation_file(f, strings)
                break
        else:
            raise ValueError("No quest book file found")

        if repo_path is None:
            print(qb_translation_file.content)
            return
        qb_translation_filepath = path.abspath(path.join(repo_path, qb_translation_file.relpath))
        with open(qb_translation_filepath, "w") as fp:
            fp.write(qb_translation_file.content)

        porcelain.add(repo_path, [qb_translation_filepath])  # type: ignore[no-untyped-call]
        commit_message = "[自动化] 更新 任务书"
        if issue is not None:
            commit_message += f"\n\nclosed #{issue}"
        porcelain.commit(  # type: ignore[no-untyped-call]
            repo_path,
            message=commit_message,
            author="MuXiu1997 <muxiu1997@gmail.com>",
        )


if __name__ == "__main__":
    fire.Fire(App, name="gtnh-translation-compare")
