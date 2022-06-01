import argparse
import shutil
import tempfile
from os import path
from pathlib import Path

from internal import ModPack, TranslationPack, ZH_DUPLICATE_KEYS, EN_DUPLICATE_KEYS, generate_translation
from utils import git_commit, set_output_and_print

RESOURCES_REL_PATH = path.join("resources")
SCRIPTS_REL_PATH = path.join("scripts")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--new-version", dest="new_version", type=str, required=True)
    parser.add_argument("--old-modpack-path", dest="old_modpack_path", type=str, required=True)
    parser.add_argument("--new-modpack-path", dest="new_modpack_path", type=str, required=True)
    parser.add_argument("--reference-path", dest="reference_path", type=str, required=True)
    parser.add_argument("--output-path", dest="output_path", type=str, required=True)
    parser.add_argument("--repo-path", dest="repo_path", type=str, required=False)
    return parser.parse_args()


if __name__ == "__main__":
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
        path.join(args.output_path, RESOURCES_REL_PATH),
    )
    if args.repo_path is not None:
        assert repo_resources_path is not None
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_resources_path = path.join(tmp_dir, RESOURCES_REL_PATH)
            shutil.copytree(repo_resources_path, tmp_resources_path)
            shutil.rmtree(repo_resources_path)
            shutil.copytree(path.join(args.output_path, RESOURCES_REL_PATH), repo_resources_path)
            shutil.copytree(path.join(tmp_resources_path, "minecraft"), path.join(repo_resources_path, "minecraft"))
            for d in Path(tmp_resources_path).glob("__other*"):
                dirname = path.basename(d)
                shutil.copytree(path.join(tmp_resources_path, dirname), path.join(repo_resources_path, dirname))
            git_commit(f"[自动化{args.new_version}]更新mod语言文件", RESOURCES_REL_PATH, args.repo_path)
    # endregion Generate new translations

    # region Generate new script file translations
    generate_translation(
        old_mod_pack.script_files,
        new_mod_pack.script_files,
        ref_translation_pack.script_files,
        path.join(args.output_path, SCRIPTS_REL_PATH),
    )
    if args.repo_path is not None:
        shutil.rmtree(path.join(args.repo_path, SCRIPTS_REL_PATH))
        shutil.copytree(path.join(args.output_path, SCRIPTS_REL_PATH), path.join(args.repo_path, SCRIPTS_REL_PATH))
        git_commit(f"[自动化{args.new_version}]更新脚本", SCRIPTS_REL_PATH, args.repo_path)
    # endregion Generate new script file translations

    # region Log DUPLICATE_KEYS
    duplicate_keys_log_content = "<details><summary>重复Key</summary>"
    for dk in (EN_DUPLICATE_KEYS, ZH_DUPLICATE_KEYS):
        for key in dk:
            if len(dk[key]) == 1:
                continue
            duplicate_keys_log_content += f"<p>Duplicate key: {key}<br>"
            for i, value in enumerate(dk[key]):
                duplicate_keys_log_content += f"\tvalue {i}: {value}<br>"
            duplicate_keys_log_content += "</p>"
    duplicate_keys_log_content += "</details>"
    set_output_and_print("duplicate-keys", duplicate_keys_log_content)
# endregion
