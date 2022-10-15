import os


def must_get_env(key: str) -> str:
    """
    Get an environment variable, or raise an exception if it is not set.

    Args:
        key: The environment variable key

    Returns:
        The environment variable value

    """
    value = os.environ.get(key)
    if value is None or value == "":
        raise Exception(f"Missing environment variable: {key}")
    return value
