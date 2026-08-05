import fnmatch
from functools import lru_cache
from typing import Callable

linebreak = "\\n"

rule = {
    "GregTech*.lang": ["/n ", "<BR>"],
    "*": ["\\n"]
}


@lru_cache
def linebreak_normalizer(path: str) -> Callable[[str], str]:
    for pattern, linebreaks in rule.items():
        if fnmatch.fnmatch(path, pattern):
            return lambda s: linebreak_map(s, linebreaks)
    return lambda s: s


@lru_cache
def linebreak_restorer(path: str) -> Callable[[str], str]:
    for pattern, linebreaks in rule.items():
        if fnmatch.fnmatch(path, pattern):
            target = linebreaks[0] if linebreaks else linebreak
            # If the target is already the canonical sequence, no change is needed.
            if target == linebreak:
                return lambda s: s
            return lambda s, t=target: s.replace(linebreak, t)

    # Pattern not found – return identity function.
    return lambda s: s


def linebreak_map(string: str, linebreaks: list[str]) -> str:
    """
    Replace every occurrence of any candidate line‑break sequence in `string`
    with the canonical `linebreak`.
    """
    for lb in linebreaks:
        string = string.replace(lb, linebreak)
    return string
