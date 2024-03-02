from typing import Iterable, Tuple


def line_iterator(content: str) -> Iterable[Tuple[int, str, int, int]]:
    """
    Iterate over lines in a string.

    Args:
        content: The content to iterate over.

    Returns:
        An iterable of tuples containing the line number, the line content, the start index and the end index.
    """
    end = 0
    for idx, line in enumerate(content.splitlines()):
        start = end + int(idx != 0)
        end = start + len(line)
        yield idx, line, start, end
