from typing import TypeAlias, Callable, NoReturn

from gtnh_translation_compare.issue.issue import Issue, new_issue_from_json
from gtnh_translation_compare.utils.env import must_get_env
from gtnh_translation_compare.utils.github_action import set_output_and_print

KEY_PASSED = "passed"
KEY_ERROR = "error"

IssueBodyLines: TypeAlias = list[str]
IssueParseFunction: TypeAlias = Callable[[IssueBodyLines], None]


class IssueParser:
    def __init__(self, issue: Issue, valid_user: str, valid_label: str):
        self.issue = issue
        self.valid_user = valid_user
        self.valid_label = valid_label
        self.check()

    @staticmethod
    def fail(e: Exception) -> NoReturn:
        set_output_and_print(KEY_PASSED, "false")
        set_output_and_print(KEY_ERROR, str(e))
        exit(1)

    def check(self) -> None:
        try:
            assert any([label.name == self.valid_label for label in self.issue.labels])
            assert self.issue.user.login == self.valid_user
        except AssertionError:
            self.fail(ValueError("Invalid user or label"))

    def parse(self, parse_function: IssueParseFunction) -> None:
        try:
            parse_function(self.issue.body.splitlines())
            set_output_and_print(KEY_PASSED, "true")
        except Exception as e:
            self.fail(e)


def new_issue_parser_from_env() -> IssueParser:
    try:
        issue_json = must_get_env("GITHUB_ISSUE")
        issue = new_issue_from_json(issue_json)
        valid_user = must_get_env("VALID_USER")
        valid_label = must_get_env("VALID_LABEL")
        return IssueParser(issue, valid_user, valid_label)
    except Exception as e:
        IssueParser.fail(e)
