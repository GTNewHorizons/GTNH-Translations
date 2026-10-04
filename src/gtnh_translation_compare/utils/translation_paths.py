from collections import defaultdict
from pathlib import Path
import subprocess

from gtnh_translation_compare.filetypes import FiletypeLang
from gtnh_translation_compare.paratranz.types import TranslationFile


def merge_case_variants(
    files: list[TranslationFile], canonical_paths: dict[str, str]
) -> list[TranslationFile]:
    groups: dict[str, list[TranslationFile]] = defaultdict(list)
    for file in files:
        groups[Path(file.relpath).as_posix().casefold()].append(file)

    result = []
    for key, variants in groups.items():
        canonical = canonical_paths.get(key)
        variants = sorted(variants, key=lambda f: (
            Path(f.relpath).as_posix() != canonical,
            sum(c.isupper() for c in f.relpath), f.relpath,
        ))
        chosen = variants[0].model_copy(deep=True)
        chosen.relpath = canonical or Path(chosen.relpath).as_posix()
        if len(variants) > 1:
            if not chosen.relpath.endswith('.lang'):
                if any(f.content != chosen.content for f in variants):
                    raise ValueError(f'Conflicting case variants: {chosen.relpath}')
            else:
                if any(f.translations is None for f in variants):
                    raise ValueError(f'Missing translation metadata: {chosen.relpath}')
                translations: dict[str, str] = {}
                for file in variants:
                    assert file.translations is not None
                    for k, value in file.translations.items():
                        if k in translations and translations[k] != value:
                            raise ValueError(f'Conflicting translations: {chosen.relpath}: {k}')
                        translations[k] = value
                properties = FiletypeLang(chosen.relpath, chosen.content).properties
                missing = translations.keys() - properties.keys()
                if missing:
                    raise ValueError(f'Translated keys missing from canonical file {chosen.relpath}: {sorted(missing)}')
                for k, prop in sorted(properties.items(), key=lambda item: item[1].start, reverse=True):
                    if k in translations:
                        chosen.content = chosen.content[:prop.start] + translations[k] + chosen.content[prop.end:]
                chosen.translations = translations
        result.append(chosen)
    return result


def remove_tracked_case_variants(repo: Path, subdirectory: Path, files: list[TranslationFile]) -> None:
    repo = repo.resolve()
    base = (repo / subdirectory).resolve()
    if not base.is_relative_to(repo):
        raise ValueError('Translation directory must be inside the repository')
    targets = {}
    for file in files:
        target = base / file.relpath
        if not target.resolve().is_relative_to(base):
            raise ValueError(f'Translation path escapes its directory: {file.relpath}')
        relative = target.relative_to(repo).as_posix()
        targets[relative.casefold()] = relative
    tracked = subprocess.check_output(
        ['git', '-C', str(repo), 'ls-files', '-z', '--', str(base)]
    ).decode('utf-8').split('\0')
    for old in tracked:
        target = targets.get(old.casefold())
        if target is None or target == old:
            continue
        old_path = repo / old
        if not old_path.resolve().is_relative_to(base):
            raise ValueError(f'Tracked alias escapes its directory: {old}')
        # On Windows both names address the same file. Remove it before writing the
        # resolved content, and remove the exact old spelling from Git's index.
        old_path.unlink(missing_ok=True)
        parent = old_path.parent
        while parent != base:
            try:
                parent.rmdir()
            except OSError:
                break
            parent = parent.parent
        subprocess.run(['git', '-C', str(repo), 'update-index', '--force-remove', '--', old], check=True)
