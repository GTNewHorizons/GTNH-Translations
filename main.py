import os
import sys

import fire  # type: ignore[import]
from loguru import logger

from gtnh_translation_compare.cmd import ParseIssue, Action


class App:
    def __init__(self) -> None:
        self.parse_issue = ParseIssue()
        self.action = Action()


def setup_logger() -> None:
    logger.remove(handler_id=None)
    logger_level = "INFO"
    if os.getenv("ACTIONS_RUNNER_DEBUG") or os.getenv("RUNNER_DEBUG") or os.getenv("GTNH_TC_DEBUG"):
        logger_level = "DEBUG"
    logger.add(sys.stderr, level=logger_level)


if __name__ == "__main__":
    setup_logger()
    fire.Fire(App, name="gtnh-translation-compare")
