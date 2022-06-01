import re

from internal import get_issue
from internal.issue import FAILED
from utils import set_output_and_print

MARKDOWN_PATTERN = re.compile(r"\[.*?]\((?P<url>.*?)\)")


def parse_gt_lang_url(markdown: str):
    match = MARKDOWN_PATTERN.match(markdown)
    assert match is not None
    return match.group("url")


if __name__ == "__main__":
    try:
        issue, passed = get_issue()

        lines = issue["body"].splitlines()

        set_output_and_print("passed", passed)
        set_output_and_print("branch", lines[2])
        set_output_and_print("gt-lang-url", parse_gt_lang_url(lines[6]))
    except Exception as e:
        set_output_and_print("passed", FAILED)
        set_output_and_print("error", str(e))
