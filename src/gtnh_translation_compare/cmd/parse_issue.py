from gtnh_translation_compare.issue.issue_parser import IssueBodyLines, new_issue_parser_from_env
from gtnh_translation_compare.utils.github_action import set_output_and_print


class ParseIssue:
    ############################################################################
    # From Paratranz
    ############################################################################

    # Quest Book
    @staticmethod
    def paratranz_to_quest_book() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("branch", lines[2])

        new_issue_parser_from_env().parse(pf)

    # Lang + Zs
    @staticmethod
    def paratranz_to_lang_and_zs() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("branch", lines[2])

        new_issue_parser_from_env().parse(pf)

    # Gt Lang
    @staticmethod
    def paratranz_to_gt_lang() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("branch", lines[2])

        new_issue_parser_from_env().parse(pf)

    ############################################################################
    # To Paratranz
    ############################################################################

    # Quest Book
    @staticmethod
    def quest_book_to_paratranz() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("commit-sha", lines[2])

        new_issue_parser_from_env().parse(pf)

    # Lang + Zs
    @staticmethod
    def lang_and_zs_to_paratranz() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("modpack-url", lines[2])

        new_issue_parser_from_env().parse(pf)

    # Gt Lang
    @staticmethod
    def gt_lang_to_paratranz() -> None:
        def pf(lines: IssueBodyLines) -> None:
            set_output_and_print("gt-lang-url", lines[2])

        new_issue_parser_from_env().parse(pf)
