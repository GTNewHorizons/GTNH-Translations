import sys

from utils import set_output

if __name__ == '__main__':
    issue_body = sys.argv[1]
    lines = issue_body.splitlines()
    set_output('old-modpack-url', lines[2])
    print(f'old-modpack-url: {lines[2]}')
    set_output('new-modpack-url', lines[6])
    print(f'new-modpack-url: {lines[6]}')
    set_output('reference-branch', lines[10])
    print(f'reference-branch: {lines[10]}')
    set_output('branch', lines[14])
    print(f'branch: {lines[14]}')
