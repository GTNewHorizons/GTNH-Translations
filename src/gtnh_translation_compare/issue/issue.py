# TODO: 使用 marshmallow 重构
from __future__ import annotations
import json

from typing import TypedDict, TypeAlias, Any, TypeGuard


class IssueUser(TypedDict):
    login: str


class IssueLabelsItem(TypedDict):
    name: str


IssueLabels: TypeAlias = list[IssueLabelsItem]
IssueBody: TypeAlias = str


class Issue(TypedDict):
    user: IssueUser
    labels: IssueLabels
    body: IssueBody


def is_valid_issue(unknown: Any) -> TypeGuard[Issue]:
    try:
        assert unknown is not None
        assert type(unknown) is dict

        assert "user" in unknown
        assert "labels" in unknown
        assert "body" in unknown

        assert type(unknown["user"]) is dict
        assert "login" in unknown["user"]
        assert type(unknown["user"]["login"]) is str

        assert type(unknown["labels"]) is list
        assert all([type(label) is dict for label in unknown["labels"]])
        assert all(["name" in label for label in unknown["labels"]])
        assert all([type(label["name"]) is str for label in unknown["labels"]])

        assert type(unknown["body"]) is str
    except AssertionError:
        return False
    return True


def new_issue_from_json(json_str: str) -> Issue:
    issue = json.loads(json_str)
    if not is_valid_issue(issue):
        raise ValueError("Invalid issue")
    return issue
