"""Check tracked paths and the combined translation payload without extracting files."""
from pathlib import Path, PurePosixPath
import json
import subprocess
from collections.abc import Iterable


def validate_paths(paths: Iterable[str]) -> None:
    seen: dict[str, tuple[str, bool]] = {}
    for name in paths:
        parts = PurePosixPath(name).parts
        for length in range(1, len(parts) + 1):
            path = '/'.join(parts[:length])
            entry = (path, length == len(parts))
            previous = seen.setdefault(path.casefold(), entry)
            if previous != entry:
                raise ValueError(f'Case or file/directory collision: {previous[0]} <> {path}')


def check_repository(root: Path) -> None:
    files = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z']).decode('utf-8').split('\0')[:-1]
    validate_paths(files)
    languages = json.loads((root / 'paratranz-projects.json').read_text(encoding='utf-8'))
    payload = []
    for name in files:
        language, _, relative = name.partition('/')
        if language in languages and (relative.startswith('config/') or relative == f'GregTech_{language}.lang'):
            payload.append(relative)
    validate_paths(payload)
    print(f'No case collisions in {len(files)} tracked files or the combined translation payload.')


if __name__ == '__main__':
    check_repository(Path(__file__).resolve().parents[2])
