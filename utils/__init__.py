import re
import subprocess

WIN_ILLEGAL_CHARS = re.compile(r'[\\/:*?"<>|]')


def replace_illegal_characters(name):
    return re.sub(WIN_ILLEGAL_CHARS, '_', name)


def set_output(key: str, value: str):
    print(f'::set-output name={key}::{value}')


def set_output_and_print(key: str, value: str):
    set_output(key, value)
    print(f'{key}={value}')


def ensure_lf(s: str):
    return '\n'.join(s.splitlines())


def git_commit(message: str, pathspec: str = '.', cwd=None):
    subprocess.run(['git', 'add', pathspec], cwd=cwd)
    subprocess.run(['git', 'commit', '-m', message], cwd=cwd)
