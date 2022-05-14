import argparse
import os
import shutil
import tempfile
from os import path
from pathlib import Path
from typing import List

from internal import ModPack, TranslationPack, Comparable
from utils import git_commit, set_output_and_print

RESOURCES_REL_PATH = path.join('resources')
SCRIPTS_REL_PATH = path.join('scripts')

EN_DUPLICATE_KEYS = dict()
ZH_DUPLICATE_KEYS = dict()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new-version', dest='new_version', type=str, required=True)
    parser.add_argument('--old-modpack-path', dest='old_modpack_path', type=str, required=True)
    parser.add_argument('--new-modpack-path', dest='new_modpack_path', type=str, required=True)
    parser.add_argument('--reference-path', dest='reference_path', type=str, required=True)
    parser.add_argument('--output-path', dest='output_path', type=str, required=True)
    parser.add_argument('--repo-path', dest='repo_path', type=str, required=False)
    return parser.parse_args()


def add_duplicate_key(k: str, v: str, _type: str):
    if _type == 'en':
        dk = EN_DUPLICATE_KEYS
    else:
        dk = ZH_DUPLICATE_KEYS
    if k not in dk:
        dk[k] = set()
    dk[k].add(v)


def collect_properties(files: List[Comparable], _type: str):
    properties = {}
    for file in files:
        for k, v in file.properties.items():
            if k in properties:
                add_duplicate_key(k, v, _type)
                add_duplicate_key(k, properties[k], _type)
            properties[k] = v
    return properties


def mark_diff(old_en: str, new_en: str, old_zh: str):
    old_zh = '\n'.join([f'// --- //{line}' for line in old_zh.splitlines()])
    new_en = '\n'.join([f'// +++ //{line}' for line in new_en.splitlines()])
    old_en = '\n'.join([f'// ↑↑↑ //{line}' for line in old_en.splitlines()])
    return f'{old_zh}\n{new_en}\n{old_en}'


def mark_new(new_en: str):
    return '\n'.join([f'// +++ //{line}' for line in new_en.splitlines()])


def mark_duplicate(en: str):
    return '\n'.join([f'// xxx //{line}' for line in en.splitlines()])


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


if __name__ == '__main__':
    args = parse_args()

    new_mod_pack = ModPack(Path(args.new_modpack_path))
    old_mod_pack = ModPack(Path(args.old_modpack_path))
    ref_translation_pack = TranslationPack(Path(args.reference_path))

    repo_resources_path = None
    if args.repo_path is not None:
        repo_resources_path = path.join(args.repo_path, RESOURCES_REL_PATH)

    # region Generate new lang file translations
    generate_translation(
        old_mod_pack.lang_files,
        new_mod_pack.lang_files,
        ref_translation_pack.lang_files,
        path.join(args.output_path, RESOURCES_REL_PATH)
    )
    if args.repo_path is not None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_resources_path = path.join(tmp_dir, RESOURCES_REL_PATH)
            shutil.copytree(repo_resources_path, tmp_resources_path)
            shutil.rmtree(repo_resources_path)
            shutil.copytree(path.join(args.output_path, RESOURCES_REL_PATH), repo_resources_path)
            shutil.copytree(path.join(tmp_resources_path, 'minecraft'), path.join(repo_resources_path, 'minecraft'))
            for d in Path(tmp_resources_path).glob('__other*'):
                dirname = path.basename(d)
                shutil.copytree(path.join(tmp_resources_path, dirname), path.join(repo_resources_path, dirname))
            git_commit(f'[自动化{args.new_version}]更新mod语言文件', RESOURCES_REL_PATH, args.repo_path)
    # endregion Generate new translations

    # region Generate new script file translations
    generate_translation(
        old_mod_pack.script_files,
        new_mod_pack.script_files,
        ref_translation_pack.script_files,
        path.join(args.output_path, SCRIPTS_REL_PATH)
    )
    if args.repo_path is not None:
        shutil.rmtree(path.join(args.repo_path, SCRIPTS_REL_PATH))
        shutil.copytree(path.join(args.output_path, SCRIPTS_REL_PATH), path.join(args.repo_path, SCRIPTS_REL_PATH))
        git_commit(f'[自动化{args.new_version}]更新脚本', SCRIPTS_REL_PATH, args.repo_path)
    # endregion Generate new script file translations

    # region Log DUPLICATE_KEYS
    duplicate_keys_log_content = '<details><summary>重复Key</summary>'
    for dk in (EN_DUPLICATE_KEYS, ZH_DUPLICATE_KEYS):
        for key in dk:
            if len(dk[key]) == 1:
                continue
            duplicate_keys_log_content += f'<p>Duplicate key: {key}<br>'
            for i, value in enumerate(dk[key]):
                duplicate_keys_log_content += f'\tvalue {i}: {value}<br>'
            duplicate_keys_log_content += '</p>'
    duplicate_keys_log_content += '</details>'
    set_output_and_print('duplicate-keys', duplicate_keys_log_content)
# endregion
