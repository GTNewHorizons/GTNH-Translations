import argparse
import os
import shutil
from os import path
from pathlib import Path
from typing import List

from internal import ModPack, TranslationPack, Comparable
from utils import get_similarity, git_commit

RESOURCES_MOD_REL_PATH = path.join('resources', 'mod')
SCRIPTS_REL_PATH = path.join('scripts')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new-version', dest='new_version', type=str, required=True)
    parser.add_argument('--old-modpack-path', dest='old_modpack_path', type=str, required=True)
    parser.add_argument('--new-modpack-path', dest='new_modpack_path', type=str, required=True)
    parser.add_argument('--reference-path', dest='reference_path', type=str, required=True)
    parser.add_argument('--output-path', dest='output_path', type=str, required=True)
    parser.add_argument('--repo-path', dest='repo_path', type=str, required=False)
    return parser.parse_args()


def log_duplicate_key(key: str, old_value: str, new_value: str):
    print(f'Duplicate key: {key}')
    print(f'First value: {old_value}')
    print(f'Second value: {new_value}')
    print()


def collect_properties(files: List[Comparable]):
    properties = {}
    for file in files:
        for k, v in file.properties.items():
            if k in properties and properties[k] != v:
                log_duplicate_key(k, properties[k], v)
            properties[k] = v
    return properties


def diff(old_en: str, new_en: str, old_zh: str):
    old_en = '\n'.join([f'# *** #{line}' for line in old_en.splitlines()])
    old_zh = '\n'.join([f'# --- #{line}' for line in old_zh.splitlines()])
    new_en = '\n'.join([f'# +++ #{line}' for line in new_en.splitlines()])
    return f'{old_en}\n{old_zh}\n{new_en}'


def generate_translation(
        old_files: List[Comparable],
        new_files: List[Comparable],
        ref_files: List[Comparable],
        output_path: str,
):
    old_properties = collect_properties(old_files)
    ref_properties = collect_properties(ref_files)

    for new_file in new_files:
        output_file_path = path.join(output_path, new_file.converted_relpath)
        os.makedirs(path.dirname(output_file_path), exist_ok=True)
        content = new_file.content
        for k, v in new_file.properties.items():
            if k in old_properties:
                if old_properties[k] == v:
                    if k in ref_properties:
                        content = content.replace(v, ref_properties[k])
                else:
                    if k in ref_properties:
                        content = content.replace(v, diff(old_properties.get(k, ''), v, ref_properties.get(k, '')))
        with open(output_file_path, 'w', encoding='utf-8') as fp:
            fp.write(content)


def get_mod_changed_paths(omp: ModPack, nmp: ModPack, tp: TranslationPack):
    ts = set()
    translation_pack_lang_relpath_list = [f.relpath for f in tp.lang_files]
    for new_file in nmp.lang_files:
        for old_file in omp.lang_files:
            if new_file.relpath != old_file.relpath:
                if (path.dirname(new_file.relpath), path.dirname(old_file.relpath)) not in ts \
                        and 0.5 < get_similarity(new_file.content, old_file.content) \
                        and old_file.converted_relpath in translation_pack_lang_relpath_list:
                    ts.add((path.dirname(old_file.relpath), path.dirname(new_file.relpath)))
    return [{'from': f, 'to': t} for f, t in sorted(ts)]


if __name__ == '__main__':
    args = parse_args()

    new_mod_pack = ModPack(Path(args.new_modpack_path))
    old_mod_pack = ModPack(Path(args.old_modpack_path))
    ref_translation_pack = TranslationPack(Path(args.reference_path))

    repo_resources_mod_path = None
    if args.repo_path is not None:
        repo_resources_mod_path = path.join(args.repo_path, RESOURCES_MOD_REL_PATH)

    # region Handle changed mod info
    mod_changed_paths = get_mod_changed_paths(old_mod_pack, new_mod_pack, ref_translation_pack)
    for changed_path in mod_changed_paths:
        _from, _to = changed_path['from'], changed_path['to']
        if args.repo_path is not None:
            if path.exists(path.join(repo_resources_mod_path, _to)):
                continue
            shutil.move(path.join(repo_resources_mod_path, _from),
                        path.join(repo_resources_mod_path, _to))
            git_commit(f'[自动化{args.new_version}]重命名文件夹 {_from} -> {_to}', RESOURCES_MOD_REL_PATH, args.repo_path)
        else:
            print(f'{_from} -> {_to}')
    # endregion Handle changed mod info

    # region Generate new lang file translations
    generate_translation(
        old_mod_pack.lang_files,
        new_mod_pack.lang_files,
        ref_translation_pack.lang_files,
        path.join(args.output_path, RESOURCES_MOD_REL_PATH)
    )
    if args.repo_path is not None:
        shutil.rmtree(repo_resources_mod_path)
        shutil.copytree(path.join(args.output_path, RESOURCES_MOD_REL_PATH), repo_resources_mod_path)
        git_commit(f'[自动化{args.new_version}]更新mod语言文件', RESOURCES_MOD_REL_PATH, args.repo_path)
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
