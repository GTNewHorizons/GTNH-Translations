import os
from os import path
from typing import List

from . import Comparable

EN_DUPLICATE_KEYS = dict()
ZH_DUPLICATE_KEYS = dict()


def generate_translation(
        old_files: List[Comparable],
        new_files: List[Comparable],
        ref_files: List[Comparable],
        output_path: str,
):
    old_properties = collect_properties(old_files, 'en')
    ref_properties = collect_properties(ref_files, 'zh')

    for new_file in new_files:
        output_file_path = path.join(output_path, new_file.converted_relpath)
        os.makedirs(path.dirname(output_file_path), exist_ok=True)
        content = new_file.content
        properties = list(new_file.properties.items())
        properties.sort(key=lambda p: len(p[0]), reverse=True)
        for k, v in properties:
            if k in old_properties:
                if old_properties[k] == v:
                    if k in ref_properties:
                        content = content.replace(v, ref_properties[k])
                else:
                    if k in ref_properties:
                        content = content.replace(v, mark_diff(old_properties.get(k, ''), v, ref_properties.get(k, '')))
            else:
                content = content.replace(v, mark_new(v))
        with open(output_file_path, 'w', encoding='utf-8') as fp:
            fp.write(content)


def collect_properties(files: List[Comparable], _type: str):
    properties = {}
    for file in files:
        for k, v in file.properties.items():
            if k in properties:
                add_duplicate_key(k, v, _type)
                add_duplicate_key(k, properties[k], _type)
            properties[k] = v
    return properties


def add_duplicate_key(k: str, v: str, _type: str):
    if _type == 'en':
        dk = EN_DUPLICATE_KEYS
    else:
        dk = ZH_DUPLICATE_KEYS
    if k not in dk:
        dk[k] = set()
    dk[k].add(v)


def mark_diff(old_en: str, new_en: str, old_zh: str):
    old_zh = '\n'.join([f'// --- //{line}' for line in old_zh.splitlines()])
    new_en = '\n'.join([f'// +++ //{line}' for line in new_en.splitlines()])
    old_en = '\n'.join([f'// ↑↑↑ //{line}' for line in old_en.splitlines()])
    return f'{old_zh}\n{new_en}\n{old_en}'


def mark_new(new_en: str):
    return '\n'.join([f'// +++ //{line}' for line in new_en.splitlines()])


def mark_duplicate(en: str):
    return '\n'.join([f'// xxx //{line}' for line in en.splitlines()])
