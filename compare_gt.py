import subprocess
from os import path

from internal import generate_translation

import argparse

from internal.gt_langfiletype import GTLangFiletype
from utils import ensure_lf, git_commit

GT_REL_PATH = 'GregTech.lang'
GT_US_REL_PATH = 'GregTech_US.lang'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-path', dest='repo_path', type=str, required=False)
    parser.add_argument('--gt-lang-url', dest='gt_lang_url', type=str, required=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    with open(path.join(args.repo_path, GT_REL_PATH), 'r') as fp:
        gt_zh = GTLangFiletype(GT_REL_PATH, ensure_lf(fp.read()))

    with open(path.join(args.repo_path, GT_US_REL_PATH), 'r') as fp:
        gt_en_old = GTLangFiletype(GT_US_REL_PATH, ensure_lf(fp.read()))

    subprocess.run(['wget', args.gt_lang_url, '-O', GT_US_REL_PATH], cwd=args.repo_path)
    git_commit(f'[自动化]更新{GT_US_REL_PATH}', GT_US_REL_PATH, args.repo_path)

    with open(path.join(args.repo_path, GT_US_REL_PATH), 'r') as fp:
        gt_en_new = GTLangFiletype(GT_US_REL_PATH, ensure_lf(fp.read()))

    generate_translation(
        [gt_en_old],
        [gt_en_new],
        [gt_zh],
        args.repo_path,
    )
    git_commit(f'[自动化]更新{GT_REL_PATH}', GT_REL_PATH, args.repo_path)
