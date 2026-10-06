"""Exercise real reconciliation in an empty disposable ParaTranz project."""
import argparse
import asyncio
import json
import os
import sys
import tempfile
from pathlib import Path

import httpx
from loguru import logger

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
# Converter imports settings; all HTTP calls use the explicit sandbox credentials below.
os.environ.setdefault('PARATRANZ_PROJECT_ID', '1')
os.environ.setdefault('PARATRANZ_TOKEN', 'unused')

from gtnh_translation_compare.filetypes import FiletypeLang, Language
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import Converter
from gtnh_translation_compare.paratranz.reconcile import reconcile_case_variants, string_snapshot

STAGES = [0, 1, 2, 3, 5, 9, -1]


async def check(project_id: int, token: str, output: Path) -> None:
    production_ids = json.loads((ROOT / 'paratranz-projects.json').read_text(encoding='utf-8')).values()
    if project_id in production_ids:
        raise ValueError('This check must never run against a production project')
    output.mkdir(parents=True, exist_ok=False)
    created_ids = set()
    requests = []
    alias_names = {}
    # The current API refuses new case-only duplicates. Map one distinct fixture's read name
    # to a legacy alias; its IDs, translation writes, verification and deletion use the real API.
    class FixtureClient(ClientWrapper):
        async def get_all_files(self):
            return [f.model_copy(update={'name': alias_names.get(f.id, f.name)})
                    for f in await super().get_all_files()]
        async def get_file(self, file_id):
            file = await super().get_file(file_id)
            return file.model_copy(update={'name': alias_names.get(file.id, file.name)})
    async def record(request):
        # Record methods and paths only; never credentials or request bodies.
        requests.append((request.method, request.url.path))
    logger.remove()
    logger.add(sys.stderr, level='WARNING')
    async with httpx.AsyncClient(base_url='https://paratranz.cn/api/', headers={'Authorization': token},
                                timeout=60, trust_env=False, event_hooks={'request': [record]}) as http:
        def client():
            return FixtureClient(http, project_id, str(output / 'cache'))
        remote = client()
        if await remote.get_all_files():
            raise ValueError('Use an empty disposable project; existing files will not be touched')
        project = await http.get(f'projects/{project_id}')
        project.raise_for_status()
        original_extra = project.json().get('extra') or {}
        try:
            # Two review passes let the sandbox represent both checked (3) and approved (5).
            settings = await http.put(f'projects/{project_id}', json={'extra': {**original_extra, 'reviewMode': 2}})
            settings.raise_for_status()
            with tempfile.TemporaryDirectory() as temporary:
                source_root = Path(temporary)
                converter = Converter(remote, None, Language.ko_KR)
                canonical_ids = []
                alias_ids = []
                for domain, existing in [('stage-existing', True), ('stage-missing', False)]:
                    relpath = f'resources/Reconciliation test[{domain}]/lang/en_US.lang'
                    text = ''.join(f'copy_{stage}=Copy stage {stage}\n' for stage in STAGES)
                    if existing:
                        text += ''.join(f'keep_{stage}=Keep stage {stage}\n' for stage in STAGES)
                        text += 'blank=Untouched untranslated entry\n'
                    source = source_root / relpath
                    source.parent.mkdir(parents=True)
                    source.write_text(text, encoding='utf-8')
                    target = await converter.to_paratranz_file(FiletypeLang(relpath, text))
                    if existing:
                        file_id = await remote.upload_file(target)
                        created_ids.add(file_id)
                        canonical_ids.append(file_id)
                        strings = await remote.get_file_strings(file_id)
                        for string in strings:
                            key = string.key.split('|', 1)[1]
                            if key.startswith('keep_'):
                                string.translation = f'Keep translation {key[5:]}'
                                string.stage = int(key[5:])
                        await remote.upload_strings([s for s in strings if s.key.split('|', 1)[1].startswith('keep_')])
                        await remote.upload_strings([s for s in strings if s.stage == 5])
                        saved_seed = await remote.get_file_strings(file_id)
                        assert string_snapshot(saved_seed) == string_snapshot(strings), 'Canonical seed stages differ'
                    alias = target.model_copy(deep=True)
                    alias.file_name = alias.file_name.replace(f'[{domain}]', f'[{domain.upper()}]')
                    legacy_name = alias.file_name
                    if existing:
                        alias.file_name = alias.file_name.replace(f'[{domain.upper()}]', f'[{domain}-fixture]')
                    alias_id = await remote.upload_file(alias)
                    created_ids.add(alias_id)
                    if existing:
                        alias_ids.append(alias_id)
                        alias_names[alias_id] = legacy_name
                    strings = await remote.get_file_strings(alias_id)
                    for string in strings:
                        key = string.key.split('|', 1)[1]
                        if key.startswith('copy_'):
                            string.translation = f'Copy translation {key[5:]}'
                            string.stage = int(key[5:])
                        elif key.startswith('keep_'):
                            string.translation = f'Keep translation {key[5:]}'
                            string.stage = 1
                    await remote.upload_strings([s for s in strings if s.translation])
                    await remote.upload_strings([s for s in strings if s.stage == 5])
                    assert string_snapshot(await remote.get_file_strings(alias_id)) == string_snapshot(strings), 'Alias seed stages differ'

                before = {file.id: {'file': file.model_dump(), 'strings': string_snapshot(await remote.get_file_strings(file.id))}
                          for file in await client().get_all_files()}
                (output / 'before.json').write_text(json.dumps(before, ensure_ascii=False, indent=2), encoding='utf-8')
                remote = client()
                converter = Converter(remote, None, Language.ko_KR)
                request_start = len(requests)
                await reconcile_case_variants(remote, converter, source_root, output / 'dry-run.json')
                assert all(method == 'GET' for method, path in requests[request_start:]), 'Dry run made a write'
                request_start = len(requests)
                await reconcile_case_variants(remote, converter, source_root, output / 'apply.json', apply=True)
                apply_requests = requests[request_start:]
                assert not any(method == 'POST' and path.endswith(f'/files/{file_id}')
                               for method, path in apply_requests for file_id in canonical_ids), 'Existing canonical file was reuploaded'
                remaining = await client().get_all_files()
                assert len(remaining) == 2 and not any(file.id in alias_ids for file in remaining), 'Redundant alias was not removed'
                assert all('[stage-existing]' in file.name or '[stage-missing]' in file.name for file in remaining), 'Case-only rename failed'
                after = {}
                for file in remaining:
                    strings = await remote.get_file_strings(file.id)
                    after[file.id] = {'file': file.model_dump(), 'strings': string_snapshot(strings)}
                    for string in strings:
                        key = string.key.split('|', 1)[1]
                        if key.startswith('copy_'):
                            assert string.translation == f'Copy translation {key[5:]}' and string.stage == int(key[5:])
                        if key.startswith('keep_') or key == 'blank':
                            old = next(s for s in before[file.id]['strings'] if s['key'] == string.key)
                            assert string.model_dump() == old, f'Untouched entry changed: {key}'
                    if file.id in canonical_ids:
                        assert file.extra == before[file.id]['file']['extra'], 'Canonical metadata changed'
                result = {'project_id': project_id, 'stages': STAGES, 'passed': True,
                          'dry_run_get_only': True, 'existing_canonical_reuploaded': False, 'existing_alias_name_mapped_for_fixture': True,
                          'after': after, 'apply_requests': apply_requests}
                (output / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
                print('PASS: all stages preserved; canonical entries and metadata unchanged; dry run GET only')
        finally:
            # Renaming retains IDs, so cleanup can stay limited to files this check created.
            try:
                files = await client().get_all_files()
                for file in files:
                    if file.id in created_ids:
                        await remote.delete_file(file.id)
            finally:
                settings = await http.put(f'projects/{project_id}', json={'extra': original_extra})
                settings.raise_for_status()
            assert not await client().get_all_files(), 'Sandbox cleanup incomplete'
            print('Sandbox cleaned; reports:', output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-id', type=int, required=True)
    parser.add_argument('--token-file', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    asyncio.run(check(args.project_id, args.token_file.read_text(encoding='utf-8-sig').strip(), args.output))
