from os import path
from typing import Tuple

from internal import get_issue
from internal.issue import FAILED
from utils import set_output_and_print


def parse_url(url: str, filename: str) -> Tuple[str, str, str]:
    if len(filename) == 0:
        filename = url.split("/")[-1]
    version = path.splitext(path.basename(filename))[0].split("-")[-1]
    return url, filename, version


if __name__ == "__main__":
    try:
        issue, passed = get_issue()

        lines = issue["body"].splitlines()
        old_modpack_url, old_modpack_name, old_version = parse_url(lines[2], lines[6])
        new_modpack_url, new_modpack_name, new_version = parse_url(lines[10], lines[14])

        set_output_and_print("passed", passed)
        set_output_and_print("old-modpack-url", old_modpack_url)
        set_output_and_print("new-modpack-url", new_modpack_url)
        set_output_and_print("old-modpack-name", old_modpack_name)
        set_output_and_print("new-modpack-name", new_modpack_name)
        set_output_and_print("old-version", old_version)
        set_output_and_print("new-version", new_version)
        set_output_and_print("reference-branch", lines[18])
        set_output_and_print("branch", lines[22])

    except Exception as e:
        set_output_and_print("passed", FAILED)
        set_output_and_print("error", str(e))
