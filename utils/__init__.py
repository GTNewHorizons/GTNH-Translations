import re
import subprocess

WIN_ILLEGAL_CHARS = re.compile(r'[\\/:*?"<>|]')


def replace_illegal_characters(name):
    return re.sub(WIN_ILLEGAL_CHARS, '_', name)


def set_output(key: str, value: str):
    print(f'::set-output name={key}::{value}')


def get_similarity(a: str, b: str):
    a_lens_set = set(a.splitlines())
    b_lens_set = set(b.splitlines())
    return len(a_lens_set & b_lens_set) / len(a_lens_set | b_lens_set)


def ensure_lf(s: str):
    return '\n'.join(s.splitlines())


def git_commit(message: str, pathspec: str = '.', cwd=None):
    subprocess.run(['git', 'add', pathspec], cwd=cwd)
    subprocess.run(['git', 'commit', '-m', message], cwd=cwd)
