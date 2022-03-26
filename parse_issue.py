import sys

from utils import set_output


def set_output_and_print(key: str, value: str):
    set_output(key, value)
    print(f'{key}={value}')


if __name__ == '__main__':
    issue_body = sys.argv[1]
    lines = issue_body.splitlines()
    old_modpack_url = lines[2]
    new_modpack_url = lines[6]
    set_output_and_print('old-modpack-url', old_modpack_url)
    set_output_and_print('new-modpack-url', new_modpack_url)
    set_output_and_print('reference-branch', lines[10])
    set_output_and_print('branch', lines[14])
    set_output_and_print('old-modpack-name', old_modpack_url.split('/')[-1])
    set_output_and_print('new-modpack-name', new_modpack_url.split('/')[-1])
