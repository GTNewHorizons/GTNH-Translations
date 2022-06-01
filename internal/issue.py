import json
import os

PASSED = "true"
FAILED = "false"


def get_issue() -> tuple[dict, str]:
    passed = FAILED

    issue_json = os.environ.get("GITHUB_ISSUE")
    assert issue_json is not None

    issue: dict = json.loads(issue_json)
    assert issue is not None
    assert type(issue) is dict

    valid_label = os.environ.get("VALID_LABEL")
    assert valid_label is not None
    valid_user = os.environ.get("VALID_USER")
    assert valid_user is not None

    if any([label["name"] == valid_label for label in issue["labels"]]) and issue["user"]["login"] == valid_user:
        passed = PASSED

    return issue, passed
