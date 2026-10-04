import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location('check_case_paths', Path(__file__).resolve().parents[2] / '.github/scripts/check_case_paths.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


@pytest.mark.parametrize('paths', [
    ['config/Foo/a.lang', 'config/foo/a.lang'],
    ['config/Foo/de_DE.lang', 'config/foo/fr_FR.lang'],
    ['config/foo', 'config/foo/de_DE.lang'],
])
def test_rejects_files_directories_and_cross_language_collisions(paths):
    with pytest.raises(ValueError, match='collision'):
        checker.validate_paths(paths)


def test_allows_shared_directories_and_distinct_language_files():
    checker.validate_paths(['config/foo/de_DE.lang', 'config/foo/fr_FR.lang', 'config/foo/de_DE.lang'])
