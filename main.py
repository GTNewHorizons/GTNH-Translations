import argparse
import os
import shutil
from os import path
from zipfile import ZipFile

from modpack import ModPack
from translationpack import TranslationPack
from utils import get_similarity, match_lang_line, git_commit

RESOURCES_MOD_REL_PATH = path.join('resources', 'mod')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--old-modpack-path', dest='old_modpack_path', type=str, required=True)
    parser.add_argument('--new-modpack-path', dest='new_modpack_path', type=str, required=True)
    parser.add_argument('--reference-path', dest='reference_path', type=str, required=True)
    parser.add_argument('--output-path', dest='output_path', type=str, required=True)
    parser.add_argument('--repo-path', dest='repo_path', type=str, required=False)
    return parser.parse_args()


def generate_translation(nmp: ModPack, omp: ModPack, tp: TranslationPack, output_dir: str):
    for relpath in nmp.lang_set.get_lang_file_relpath_list():
        output_file_relpath = relpath.replace('en_US', 'zh_CN')
        output_file_path = path.join(output_dir, output_file_relpath)
        os.makedirs(path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w') as fp:
            if omp.lang_set.get_content(relpath) == nmp.lang_set.get_content(relpath):
                fp.write(tp.lang_set.get_content(output_file_relpath, ''))
            else:
                result = []
                for line in nmp.lang_set.get_content(relpath).splitlines():
                    key, _ = match_lang_line(line)
                    if key is not None:
                        if nmp.lang_set.get_value(key) == omp.lang_set.get_value(key):
                            if tp.lang_set.get_value(key) is not None:
                                result.append(f'{key}={tp.lang_set.get_value(key)}')
                                continue
                    result.append(line)
                fp.writelines(result)


def get_changed_paths(omp: ModPack, nmp: ModPack, tp: TranslationPack):
    ts = set()
    for key in nmp.lang_set.get_keys():
        new_relpath = nmp.lang_set.get_relpath_by_key(key)
        old_relpath = omp.lang_set.get_relpath_by_key(key)
        if new_relpath != old_relpath and old_relpath is not None:
            if (path.dirname(old_relpath), path.dirname(new_relpath)) not in ts:
                if 0.5 < get_similarity(
                        omp.lang_set.get_content(old_relpath),
                        b=nmp.lang_set.get_content(new_relpath)
                ):
                    if tp.lang_set.get_content(old_relpath.replace('en_US', 'zh_CN')) is not None:
                        ts.add((path.dirname(old_relpath), path.dirname(new_relpath)))
    return [{'from': f, 'to': t} for f, t in sorted(ts)]


if __name__ == '__main__':
    args = parse_args()

    new_mod_pack = ModPack(ZipFile(args.new_modpack_path))
    old_mod_pack = ModPack(ZipFile(args.old_modpack_path))
    ref_translation_pack = TranslationPack(args.reference_path)

    repo_resources_mod_path = None
    if args.repo_path is not None:
        repo_resources_mod_path = path.join(args.repo_path, RESOURCES_MOD_REL_PATH)

    # region Handle changed mod info
    changed_paths = get_changed_paths(old_mod_pack, new_mod_pack, ref_translation_pack)
    if args.repo_path is not None:
        for changed_path in changed_paths:
            _from, _to = changed_path['from'], changed_path['to']
            if path.exists(path.join(repo_resources_mod_path, _to)):
                continue
            shutil.move(path.join(repo_resources_mod_path, _from),
                        path.join(repo_resources_mod_path, _to))
            git_commit(f'重命名文件夹 {_from} -> {_to}', RESOURCES_MOD_REL_PATH, args.repo_path)
    else:
        for changed_path in changed_paths:
            print(f'{changed_path["from"]} -> {changed_path["to"]}')
    # endregion Handle changed mod info

    # region Generate new translations
    generate_translation(new_mod_pack, old_mod_pack, ref_translation_pack, args.output_path)
    if args.repo_path is not None:
        shutil.rmtree(repo_resources_mod_path)
        shutil.copytree(args.output_path, repo_resources_mod_path)
        git_commit('更新mod语言文件', RESOURCES_MOD_REL_PATH, args.repo_path)
    # endregion Generate new translations
