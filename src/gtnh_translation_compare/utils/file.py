import re

WIN_ILLEGAL_CHARS = re.compile(r'[\\/:*?"<>|]')


def replace_illegal_characters(name: str) -> str:
    """
    Replaces illegal characters in a string with an underscore.

    Args:
        name: string that may contain illegal characters

    Returns:
        string with illegal characters replaced with an underscore
    """
    return re.sub(WIN_ILLEGAL_CHARS, "_", name)


def ensure_lf(s: str) -> str:
    """
    Ensure a multi-line string is made up of LF as a line break.

    Args:
        s: multi-line string

    Returns:
        multi-line string with LF as a line break
    """
    return "\n".join(s.splitlines())
