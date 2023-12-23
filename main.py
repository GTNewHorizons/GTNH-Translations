import os
import sys

import fire  # type: ignore[import]
from loguru import logger

from gtnh_translation_compare.cmd import ParseIssue, Action


class App:
    def __init__(self) -> None:
        self.parse_issue = ParseIssue()
        self.action = Action()


if __name__ == "__main__":
    if os.environ.get("GTNH_TC_DEBUG") is None:
        logger.remove(handler_id=None)
        logger.add(sys.stderr, level="INFO")
    fire.Fire(App, name="gtnh-translation-compare")
