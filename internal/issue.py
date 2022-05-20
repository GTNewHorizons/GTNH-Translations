import json
import os


def get_issue() -> (dict, str):
    issue = json.loads(os.environ.get('GITHUB_ISSUE'))
    valid_label = os.environ.get('VALID_LABEL')
    valid_user = os.environ.get('VALID_USER')

    passed = 'false'
    if any([label['name'] == valid_label for label in issue['labels']]) and issue['user']['login'] == valid_user:
        passed = 'true'

    return issue, passed
