import shutil
from os import path
import sys

base_temp_path = 'temp'


def copy_item(src_path, dest_path):
    if path.isdir(src_path):
        shutil.copytree(src_path, dest_path)
    else:
        shutil.copy(src_path, dest_path)


def main(language):
    paths_to_be_packed = [
        'config',
        f'GregTech_{language}.lang',
    ]
    for p in paths_to_be_packed:
        src_path = path.join(language, p)
        dest_path = path.join(base_temp_path, p)
        copy_item(src_path, dest_path)


if __name__ == '__main__':
    main(sys.argv[1])
