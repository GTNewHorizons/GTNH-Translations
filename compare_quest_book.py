import subprocess
from os import path

from internal import generate_translation

import argparse

from internal.langfiletype import LangFiletype
from utils import ensure_lf, git_commit

GTNH_REPO = "https://github.com/GTNewHorizons/GT-New-Horizons-Modpack"
GTNH_DEFAULT_QUESTS_US_REL_PATH = "config/betterquesting/DefaultQuests-us.json"
DEFAULT_QUESTS_REL_PATH = "config/betterquesting/DefaultQuests.json"
LANG_REL_PATH = "resources/minecraft/lang/zh_CN.lang"
LANG_US_REL_PATH = "resources/minecraft/lang/en_US.lang"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-path", dest="repo_path", type=str, required=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # noinspection DuplicatedCode
    subprocess.run(
        [
            "wget",
            f"{GTNH_REPO}/raw/master/{GTNH_DEFAULT_QUESTS_US_REL_PATH}",
            "-O",
            DEFAULT_QUESTS_REL_PATH,
        ],
        cwd=args.repo_path,
    )
    git_commit(f"[自动化]更新{DEFAULT_QUESTS_REL_PATH}", DEFAULT_QUESTS_REL_PATH, args.repo_path)

    with open(path.join(args.repo_path, LANG_REL_PATH), "r") as fp:
        lang_zh = LangFiletype(LANG_REL_PATH, ensure_lf(fp.read()))

    with open(path.join(args.repo_path, LANG_US_REL_PATH), "r") as fp:
        lang_en_old = LangFiletype(LANG_US_REL_PATH, ensure_lf(fp.read()))

    # noinspection DuplicatedCode
    subprocess.run(
        [
            "wget",
            f"{GTNH_REPO}/raw/master/{LANG_US_REL_PATH}",
            "-O",
            LANG_US_REL_PATH,
        ],
        cwd=args.repo_path,
    )
    git_commit(f"[自动化]更新{LANG_US_REL_PATH}", LANG_US_REL_PATH, args.repo_path)

    with open(path.join(args.repo_path, LANG_US_REL_PATH), "r") as fp:
        lang_en_new = LangFiletype(LANG_US_REL_PATH, ensure_lf(fp.read()))

    generate_translation(
        [lang_en_old],
        [lang_en_new],
        [lang_zh],
        args.repo_path,
    )
    git_commit(f"[自动化]更新{LANG_REL_PATH}", LANG_REL_PATH, args.repo_path)
