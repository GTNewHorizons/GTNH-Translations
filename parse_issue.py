import sys

from utils import set_output

if __name__ == '__main__':
    issue_body = sys.argv[1]
    lines = issue_body.splitlines()
    old_modpack_url = lines[2]
    set_output('old-modpack-url', old_modpack_url)
    print(f'old-modpack-url: {old_modpack_url}')
    new_modpack_url = lines[6]
    set_output('new-modpack-url', new_modpack_url)
    print(f'new-modpack-url: {new_modpack_url}')
    set_output('reference-branch', lines[10])
    print(f'reference-branch: {lines[10]}')
    set_output('branch', lines[14])
    print(f'branch: {lines[14]}')
    old_modpack_name = old_modpack_url.split('/')[-1]
    set_output('old-modpack-name', old_modpack_name)
    print(f'old-modpack-name: {old_modpack_name}')
    new_modpack_name = new_modpack_url.split('/')[-1]
    set_output('new-modpack-name', new_modpack_name)
    print(f'new-modpack-name: {new_modpack_name}')
