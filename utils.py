import re

WIN_ILLEGAL_CHARS = re.compile(r'[\\/:*?"<>|]')


def replace_illegal_characters(name):
    return re.sub(WIN_ILLEGAL_CHARS, '_', name)


def set_output(key: str, value: str):
    print('::set-output name={}::{}'.format(key, value))
