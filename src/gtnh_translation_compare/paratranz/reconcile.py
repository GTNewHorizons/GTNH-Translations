"""Reconcile case-only ParaTranz aliases against the current English sources."""
import json
from collections import defaultdict
from pathlib import Path

from loguru import logger

from gtnh_translation_compare.filetypes import FiletypeLang
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import Converter
from gtnh_translation_compare.paratranz.types import File, ParatranzFile, StringItem


def merge_strings(target: ParatranzFile, snapshots: list[tuple[File, list[StringItem]]]) -> None:
    by_key = {s.key: s for s in target.string_items}
    # Prefer the canonical file's review stage when identical translations exist.
    for file, strings in sorted(snapshots, key=lambda item: (item[0].name != target.file_name, item[0].name)):
        for string in strings:
            if not string.translation:
                continue
            destination = by_key.get(string.key)
            if destination is None or destination.original != string.original:
                raise ValueError(f'{file.name}: translated key needs review against current source: {string.key}')
            if destination.translation and destination.translation != string.translation:
                raise ValueError(f'{file.name}: conflicting translations: {string.key}')
            if not destination.translation:
                destination.translation = string.translation
                destination.stage = string.stage


def string_snapshot(strings: list[StringItem]) -> list[dict]:
    return [s.model_dump() for s in sorted(strings, key=lambda s: s.key)]


async def reconcile_case_variants(
    client: ClientWrapper, converter: Converter, source_root: Path, backup_path: Path, apply: bool = False
) -> None:
    sources = {
        FiletypeLang(p.relative_to(source_root).as_posix(), '').get_target_language_relpath(converter.target_lang) + '.json': p
        for p in (source_root / 'resources').glob('*/lang/en_US.lang')
    }
    if not sources:
        raise ValueError(f'No current English mod language files under {source_root}')
    canonical_names = {name.casefold(): name for name in sources}
    groups: dict[str, list[File]] = defaultdict(list)
    for file in await client.get_all_files():
        canonical = canonical_names.get(file.name.casefold())
        if canonical:
            groups[canonical].append(file)

    plans = []
    report = {'project_id': client.project_id, 'apply': apply, 'groups': [], 'conflicts': []}
    for canonical, files in sorted(groups.items()):
        if all(f.name == canonical for f in files):
            continue
        snapshots = [(await client.get_file(f.id), await client.get_strings(f.id)) for f in files]
        source = sources[canonical]
        target = await converter.to_paratranz_file(FiletypeLang(
            source.relative_to(source_root).as_posix(), source.read_text(encoding='utf-8')
        ))
        entry = {
            'canonical': canonical,
            'files': [{'file': f.model_dump(), 'strings': string_snapshot(strings)} for f, strings in snapshots],
        }
        report['groups'].append(entry)
        try:
            if any(f.name.casefold() != canonical.casefold() for f, _ in snapshots):
                raise ValueError(f'File renamed during preflight: {canonical}')
            merge_strings(target, snapshots)
        except ValueError as error:
            report['conflicts'].append(str(error))
            continue
        plans.append((target, snapshots))
        logger.info('Reconcile {}: {} alias(es), {} translated keys', canonical,
                    sum(f.name != canonical for f, _ in snapshots), sum(bool(s.translation) for s in target.string_items))

    backup_path.parent.mkdir(parents=True, exist_ok=True)
    # Never replace an earlier backup, including one made by an interrupted apply.
    with backup_path.open('x', encoding='utf-8') as output:
        json.dump(report, output, ensure_ascii=False, indent=2)
    if report['conflicts']:
        raise ValueError('No files changed; resolve conflicts in ' + str(backup_path))
    if not apply:
        logger.info('Dry run complete; backup and plan: {}', backup_path)
        return

    for target, snapshots in plans:
        # Refuse to overwrite edits made since the preflight snapshot.
        for file, strings in snapshots:
            current = await client.get_file(file.id)
            if current.name != file.name or current.extra != file.extra or string_snapshot(await client.get_strings(file.id)) != string_snapshot(strings):
                raise ValueError(f'ParaTranz changed during reconciliation: {file.name}')
        target_id = await client.upload_file(target)
        if target_id is None:
            raise ValueError(f'No canonical file created: {target.file_name}')
        saved = {s.key: s for s in await client.get_strings(target_id)}
        for planned in target.string_items:
            actual = saved.get(planned.key)
            if actual is None or actual.original != planned.original or actual.translation != planned.translation:
                raise ValueError(f'Canonical verification failed; aliases retained: {target.file_name}: {planned.key}')
            if planned.translation and actual.stage != planned.stage:
                raise ValueError(f'Review stage verification failed; aliases retained: {target.file_name}: {planned.key}')
        for file, strings in snapshots:
            if file.id == target_id:
                continue
            current = await client.get_file(file.id)
            if current.name != file.name or current.extra != file.extra or string_snapshot(await client.get_strings(file.id)) != string_snapshot(strings):
                raise ValueError(f'Alias changed; retained: {file.name}')
            await client.delete_file(file.id)
        logger.info('Reconciled {}', target.file_name)
