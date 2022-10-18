from typing import Optional

import fire  # type: ignore[import]
import requests
from paratranz_client.client import AuthenticatedClient

from gtnh_translation_compare.filetypes import FiletypeLang, Language
from gtnh_translation_compare.issue.issue_parser import IssueBodyLines, new_issue_parser_from_env
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import to_paratranz_file
from gtnh_translation_compare.utils.env import must_get_env
from gtnh_translation_compare.utils.github_action import set_output_and_print

GTNH_REPO = "https://github.com/GTNewHorizons/GT-New-Horizons-Modpack"
DEFAULT_QUESTS_LANG_US_REL_PATH = "resources/minecraft/lang/en_US.lang"


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
        qb_json_file_url = f"{GTNH_REPO}/raw/{commit_sha}/{DEFAULT_QUESTS_LANG_US_REL_PATH}"
        res = requests.get(qb_json_file_url)
        qb_lang_file = FiletypeLang(relpath=DEFAULT_QUESTS_LANG_US_REL_PATH, content=res.text, language=Language.en_US)
        qb_paratranz_file = to_paratranz_file(qb_lang_file)
        self.client.upload_file(qb_paratranz_file)


if __name__ == "__main__":
    fire.Fire(App)
