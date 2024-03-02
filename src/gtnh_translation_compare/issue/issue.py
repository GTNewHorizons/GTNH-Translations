from typing import List

from pydantic import BaseModel


class IssueUser(BaseModel):
    login: str


class IssueLabelsItem(BaseModel):
    name: str


class Issue(BaseModel):
    user: IssueUser
    labels: List[IssueLabelsItem]
    body: str


def new_issue_from_json(json_str: str) -> Issue:
    return Issue.model_validate_json(json_str)
