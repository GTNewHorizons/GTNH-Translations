import argparse
import os
import shutil
import subprocess
from os import path
from zipfile import ZipFile

from langset import LANG_LINE_PATTERN
from modpack import ModPack
from translationpack import TranslationPack
from utils import get_similarity


def generate_translation(nmp: ModPack, omp: ModPack, tp: TranslationPack, output_dir: str):
    for file_name in nmp.lang_map.keys():
        output_file_name = file_name.replace('en_US', 'zh_CN')
        output_file_path = path.join(output_dir, output_file_name)
        os.makedirs(path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w') as fp:
            if omp.lang_map.get(file_name) == nmp.lang_map.get(file_name):
                fp.write(tp.lang_map.get(output_file_name, ''))
            else:
                for line in nmp.lang_map.get(file_name).splitlines():
                    m = LANG_LINE_PATTERN.match(line)
                    if m is not None:
                        key = m.group(1)
                        if nmp.lang_key_value_map.get(key) == omp.lang_key_value_map.get(key):
                            if tp.lang_key_value_map.get(key) is not None:
                                fp.write(f'{key}={tp.lang_key_value_map.get(key)}\n')
                                continue
                    fp.write(line + '\n')


def get_changed_paths(omp: ModPack, nmp: ModPack, rtp: TranslationPack):
    ts = set()
    for key in nmp.lang_key_file_map.keys():
        nf = nmp.lang_key_file_map.get(key)
        of = omp.lang_key_file_map.get(key)
        if nf != of and of is not None:
            if (path.dirname(of), path.dirname(nf)) not in ts:
                if 0.5 < get_similarity(a=omp.lang_map.get(of), b=nmp.lang_map.get(nf)):
                    if rtp.lang_map.get(of.replace('en_US', 'zh_CN')) is not None:
                        ts.add((path.dirname(of), path.dirname(nf)))
    return [{'from': f, 'to': t} for f, t in sorted(ts)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--old-modpack-path', dest='old_modpack_path', type=str, required=True)
    parser.add_argument('--new-modpack-path', dest='new_modpack_path', type=str, required=True)
    parser.add_argument('--reference-path', dest='reference_path', type=str, required=True)
    parser.add_argument('--output-path', dest='output_path', type=str, required=True)
    parser.add_argument('--repo-path', dest='repo_path', type=str, required=False)
    args = parser.parse_args()

    new_mod_pack = ModPack(ZipFile(args.new_modpack_path))
    old_mod_pack = ModPack(ZipFile(args.old_modpack_path))
    ref_translation_pack = TranslationPack(args.reference_path)
    resources_mod_rel_path = path.join('resources', 'mod')
    resources_mod_path = None
    if args.repo_path is not None:
        resources_mod_path = path.join(args.repo_path, resources_mod_rel_path)

    changed_paths = get_changed_paths(old_mod_pack, new_mod_pack, ref_translation_pack)
    if args.repo_path is not None:
        for m in changed_paths:
            if path.exists(path.join(resources_mod_path, m['to'])):
                continue
            shutil.move(path.join(resources_mod_path, m['from']), path.join(resources_mod_path, m['to']))
            subprocess.run(['git', 'add', resources_mod_rel_path], cwd=args.repo_path)
            subprocess.run(['git', 'commit', '-m', f'重命名文件夹 {m["from"]} -> {m["to"]}'], cwd=args.repo_path)
    else:
        for m in changed_paths:
            print(f'{m["from"]} -> {m["to"]}')

    generate_translation(new_mod_pack, old_mod_pack, ref_translation_pack, args.output_path)
    if args.repo_path is not None:
        shutil.rmtree(resources_mod_path)
        shutil.copytree(args.output_path, resources_mod_path)
        subprocess.run(['git', 'add', resources_mod_rel_path], cwd=args.repo_path)
        subprocess.run(['git', 'commit', '-m', '更新mod语言文件'], cwd=args.repo_path)
