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
        snapshots = [(await client.get_file(f.id), await client.get_file_strings(f.id)) for f in files]
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
            destination = next(((f, strings) for f, strings in snapshots if f.name == canonical), None)
            if destination is None:
                # Reuse a source-compatible alias: ParaTranz rejects creating a case-only duplicate.
                for file, strings in sorted(snapshots, key=lambda item: (item[0].name, item[0].id)):
                    existing = {s.key: s for s in strings}
                    if all(s.key in existing and existing[s.key].original == s.original for s in target.string_items):
                        destination = file, strings
                        break
            if destination is None:
                raise ValueError(f'No alias has the current source; source sync required: {canonical}')
            existing = {s.key: s for s in destination[1]}
            if any(s.key not in existing or existing[s.key].original != s.original for s in target.string_items):
                raise ValueError(f'Canonical file needs source sync before reconciliation: {canonical}')
            entry['destination_file_id'] = destination[0].id
            entry['rename'] = destination[0].name != canonical
            entry['copied_keys'] = [s.key for s in target.string_items if s.translation and not existing[s.key].translation]
        except ValueError as error:
            report['conflicts'].append(str(error))
            continue
        plans.append((target, snapshots, destination))
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

    for target, snapshots, destination in plans:
        # Refuse to overwrite edits made since the preflight snapshot.
        for file, strings in snapshots:
            current = await client.get_file(file.id)
            if current.name != file.name or current.extra != file.extra or string_snapshot(await client.get_file_strings(file.id)) != string_snapshot(strings):
                raise ValueError(f'ParaTranz changed during reconciliation: {file.name}')
        file, original_strings = destination
        target_id = file.id
        expected_file = file
        if file.name != target.file_name:
            await client.rename_file(target_id, target)
            expected_file = file.model_copy(update={'name': target.file_name, 'extra': target.file_extra.model_dump()})
        existing = {s.key: s for s in original_strings}
        updates = []
        for planned in target.string_items:
            actual = existing.get(planned.key)
            if actual is None or actual.original != planned.original or actual.id is None:
                raise ValueError(f'Canonical source verification failed; aliases retained: {target.file_name}: {planned.key}')
            if actual.translation and actual.translation != planned.translation:
                raise ValueError(f'Canonical translation changed; aliases retained: {target.file_name}: {planned.key}')
            if planned.translation and not actual.translation:
                updates.append(actual.model_copy(update={'translation': planned.translation, 'stage': planned.stage}))
        expected = dict(existing)
        expected.update({s.key: s for s in updates})
        if updates:
            await client.upload_strings(updates)
        saved = {s.key: s for s in await client.get_file_strings(target_id)}
        # With two review passes, the first approved write becomes checked; a second confirms approval.
        approvals = [s for s in updates if s.stage == 5 and saved.get(s.key) == s.model_copy(update={'stage': 3})]
        if approvals:
            await client.upload_strings(approvals)
            saved = {s.key: s for s in await client.get_file_strings(target_id)}
        current_file = await client.get_file(target_id)
        if current_file.name != expected_file.name or current_file.extra != expected_file.extra:
            raise ValueError(f'Canonical file changed; aliases retained: {target.file_name}')
        # Verify copied stages and every untouched entry before deleting any alias.
        if string_snapshot(list(saved.values())) != string_snapshot(list(expected.values())):
            raise ValueError(f'Canonical verification failed; aliases retained: {target.file_name}')
        for file, strings in snapshots:
            if file.id == target_id:
                continue
            current = await client.get_file(file.id)
            if current.name != file.name or current.extra != file.extra or string_snapshot(await client.get_file_strings(file.id)) != string_snapshot(strings):
                raise ValueError(f'Alias changed; retained: {file.name}')
            await client.delete_file(file.id)
        logger.info('Reconciled {}', target.file_name)
