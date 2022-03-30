import json
import os
from os import path

from utils import set_output


def set_output_and_print(key: str, value: str):
    set_output(key, value)
    print(f'{key}={value}')


def parse_url(url) -> (str, str, str):
    filename = url.split('/')[-1]
    version = path.splitext(path.basename(filename))[0].split('-')[-1]
    return url, filename, version


if __name__ == '__main__':
    issue = json.loads(os.environ.get('GITHUB_ISSUE'))
    valid_label = os.environ.get('VALID_LABEL')
    valid_user = os.environ.get('VALID_USER')

    passed = 'false'
    if any([label['name'] == valid_label for label in issue['labels']]) and issue['user']['login'] == valid_user:
        passed = 'true'

    lines = issue['body'].splitlines()
    old_modpack_url, old_modpack_name, old_version = parse_url(lines[2])
    new_modpack_url, new_modpack_name, new_version = parse_url(lines[6])

    set_output_and_print('passed', passed)
    set_output_and_print('old-modpack-url', old_modpack_url)
    set_output_and_print('new-modpack-url', new_modpack_url)
    set_output_and_print('old-modpack-name', old_modpack_name)
    set_output_and_print('new-modpack-name', new_modpack_name)
    set_output_and_print('old-version', old_version)
    set_output_and_print('new-version', new_version)
    set_output_and_print('reference-branch', lines[10])
    set_output_and_print('branch', lines[14])
