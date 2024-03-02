def to_unicode(s: str) -> str:
    """
    Convert a string to a unicode string.

    Args:
        s: The string to convert.

    Returns:
        The unicode string.
    """
    return "".join(["\\u%04x" % ord(c) for c in s])
