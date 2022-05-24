from internal import get_issue
from utils import set_output_and_print

if __name__ == '__main__':
    issue, passed = get_issue()

    lines = issue['body'].splitlines()

    set_output_and_print('passed', passed)
    set_output_and_print('branch', lines[2])
