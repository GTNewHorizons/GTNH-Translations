from internal import get_issue
from internal.issue import FAILED
from utils import set_output_and_print

if __name__ == "__main__":
    try:
        issue, passed = get_issue()

        lines = issue["body"].splitlines()

        set_output_and_print("passed", passed)
        set_output_and_print("branch", lines[2])

    except Exception as e:
        set_output_and_print("passed", FAILED)
        set_output_and_print("error", str(e))
