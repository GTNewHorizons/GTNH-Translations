import asyncio
import json
from pathlib import Path

import httpx
import pytest

from gtnh_translation_compare.filetypes import FiletypeLang, Language
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import Converter
from gtnh_translation_compare.paratranz.reconcile import reconcile_case_variants
from gtnh_translation_compare.paratranz.types import File, StringItem


CANONICAL = 'resources/BetterQuesting[cb4bq]/lang/ko_KR.lang.json'
ALIAS = CANONICAL.replace('[cb4bq]', '[CB4BQ]')


class Client:
    project_id = 1

    def __init__(self, fail_verification=False, conflict=False, missing_target=False):
        self.files = {1: File(id=1, name=ALIAS), 2: File(id=2, name=CANONICAL)}
        self.strings = {
            1: [StringItem(id=11, key='lang|name', original='English', translation='번역', stage=5)],
            2: [StringItem(id=22, key='lang|name', original='English', translation='Conflict' if conflict else '', stage=0)],
        }
        if missing_target:
            del self.files[2]
            del self.strings[2]
        self.events = []
        self.fail_verification = fail_verification

    async def get_all_files(self):
        return list(self.files.values())

    async def get_file(self, file_id):
        return self.files[file_id].model_copy(deep=True)

    async def get_file_strings(self, file_id):
        return [s.model_copy(deep=True) for s in self.strings[file_id]]

    async def rename_file(self, file_id, target):
        self.events.append('rename')
        self.files[file_id] = File(id=file_id, name=target.file_name, extra=target.file_extra.model_dump())

    async def upload_strings(self, strings):
        self.events.append('strings')
        for update in strings:
            for i, existing in enumerate(self.strings[2]):
                if existing.id == update.id:
                    self.strings[2][i] = update.model_copy(deep=True)
        if self.fail_verification:
            self.strings[2][0].stage = 1

    async def delete_file(self, file_id):
        self.events.append('delete')
        assert self.strings[2][0].translation == '번역'
        del self.files[file_id]


def run(tmp_path, client, apply=False):
    source = tmp_path / 'daily-history/resources/BetterQuesting[cb4bq]/lang/en_US.lang'
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text('name=English\n', encoding='utf-8')
    backup = tmp_path / 'backup.json'
    converter = Converter(client, None, Language.ko_KR)
    asyncio.run(reconcile_case_variants(client, converter, tmp_path / 'daily-history', backup, apply=apply))
    return json.loads(backup.read_text(encoding='utf-8'))


def test_dry_run_backs_up_without_writes(tmp_path):
    client = Client()
    report = run(tmp_path, client)
    assert client.events == []
    assert report['groups'][0]['canonical'] == CANONICAL
    assert report['groups'][0]['files'][0]['strings'][0]['translation'] == '번역'


@pytest.mark.parametrize('missing_target', [False, True])
def test_apply_preserves_translation_and_stage_before_deleting_alias(tmp_path, missing_target):
    client = Client(missing_target=missing_target)
    run(tmp_path, client, apply=True)
    assert client.events == (['rename'] if missing_target else ['strings', 'delete'])
    destination_id = 1 if missing_target else 2
    assert list(client.files) == [destination_id]
    assert client.files[destination_id].name == CANONICAL
    assert client.strings[destination_id][0].stage == 5


def test_failed_readback_never_deletes_alias(tmp_path):
    client = Client(fail_verification=True)
    with pytest.raises(ValueError, match='verification failed'):
        run(tmp_path, client, apply=True)
    assert client.events == ['strings']
    assert 1 in client.files
    assert (tmp_path / 'backup.json').exists()


def test_conflict_is_reported_before_any_write(tmp_path):
    client = Client(conflict=True)
    with pytest.raises(ValueError, match='No files changed'):
        run(tmp_path, client, apply=True)
    assert client.events == []
    report = json.loads((tmp_path / 'backup.json').read_text(encoding='utf-8'))
    assert 'conflicting translations' in report['conflicts'][0]


def test_apply_refuses_changes_since_preflight(tmp_path):
    class EditedClient(Client):
        reads = 0
        async def get_file_strings(self, file_id):
            strings = await super().get_file_strings(file_id)
            self.reads += 1
            if self.reads > 2 and file_id == 1:
                strings[0].translation = 'New edit'
            return strings
    client = EditedClient()
    with pytest.raises(ValueError, match='changed during reconciliation'):
        run(tmp_path, client, apply=True)
    assert client.events == []


def test_existing_backup_is_not_overwritten(tmp_path):
    (tmp_path / 'backup.json').write_text('previous backup', encoding='utf-8')
    client = Client()
    with pytest.raises(FileExistsError):
        run(tmp_path, client, apply=True)
    assert client.events == []
    assert (tmp_path / 'backup.json').read_text() == 'previous backup'


def test_delete_file_uses_scoped_endpoint_and_checks_errors(tmp_path):
    requests = []
    def handle(request):
        requests.append((request.method, request.url.path))
        return httpx.Response(403)
    client = ClientWrapper(httpx.AsyncClient(transport=httpx.MockTransport(handle), base_url='https://paratranz.cn/api'), 1, str(tmp_path))
    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(client.delete_file(17))
    assert requests == [('DELETE', '/api/projects/1/files/17')]


@pytest.mark.parametrize('source_change', ['original', 'key'])
def test_translated_keys_with_changed_or_missing_sources_block_all_writes(tmp_path, source_change):
    client = Client()
    if source_change == 'original':
        client.strings[1][0].original = 'Outdated English'
    else:
        client.strings[1][0].key = 'lang|removed'
    with pytest.raises(ValueError, match='No files changed'):
        run(tmp_path, client, apply=True)
    assert client.events == []
    report = json.loads((tmp_path / 'backup.json').read_text(encoding='utf-8'))
    assert 'needs review against current source' in report['conflicts'][0]


def test_existing_canonical_entries_and_metadata_are_untouched(tmp_path):
    client = Client()
    client.files[2].extra = {'canonical': 'metadata'}
    client.strings[2].append(StringItem(id=23, key='lang|old', original='Old', translation='', stage=9))
    original = client.strings[2][1].model_copy(deep=True)
    run(tmp_path, client, apply=True)
    assert client.events == ['strings', 'delete']
    assert client.strings[2][1] == original
    assert client.files[2].extra == {'canonical': 'metadata'}


def test_identical_translation_keeps_canonical_stage_without_writes(tmp_path):
    client = Client()
    client.strings[2][0].translation = '번역'
    client.strings[2][0].stage = 3
    run(tmp_path, client, apply=True)
    assert client.events == ['delete']
    assert client.strings[2][0].stage == 3


def test_outdated_canonical_source_blocks_writes_in_preflight(tmp_path):
    client = Client()
    client.strings[2][0].original = 'Old English'
    with pytest.raises(ValueError, match='No files changed'):
        run(tmp_path, client, apply=True)
    assert client.events == []
    report = json.loads((tmp_path / 'backup.json').read_text(encoding='utf-8'))
    assert 'needs source sync' in report['conflicts'][0]


def test_side_effect_on_untouched_entry_retains_alias(tmp_path):
    class SideEffectClient(Client):
        async def upload_strings(self, strings):
            await super().upload_strings(strings)
            self.strings[2][1].stage = 1
    client = SideEffectClient()
    client.strings[2].append(StringItem(id=23, key='lang|old', original='Old', translation='', stage=9))
    with pytest.raises(ValueError, match='verification failed'):
        run(tmp_path, client, apply=True)
    assert client.events == ['strings']
    assert 1 in client.files


def test_file_string_snapshot_includes_hidden_entries(tmp_path):
    requests = []
    def handle(request):
        requests.append((request.method, request.url.path))
        return httpx.Response(200, json=[{
            'id': 42, 'key': 'hidden', 'original': 'English', 'translation': 'Hidden translation', 'stage': -1,
        }])
    http = httpx.AsyncClient(transport=httpx.MockTransport(handle), base_url='https://paratranz.cn/api/')
    client = ClientWrapper(http, 1, str(tmp_path))
    strings = asyncio.run(client.get_file_strings(17))
    assert strings[0].id == 42 and strings[0].stage == -1
    assert requests == [('GET', '/api/projects/1/files/17/translation')]


def test_two_review_passes_confirm_approval_after_checked_readback(tmp_path):
    class TwoPassClient(Client):
        async def upload_strings(self, strings):
            first_write = 'strings' not in self.events
            await super().upload_strings(strings)
            if first_write:
                self.strings[2][0].stage = 3
    client = TwoPassClient()
    run(tmp_path, client, apply=True)
    assert client.events == ['strings', 'strings', 'delete']
    assert client.strings[2][0].stage == 5


def test_missing_canonical_with_incomplete_alias_blocks_before_rename(tmp_path):
    client = Client(missing_target=True)
    client.strings[1] = []
    with pytest.raises(ValueError, match='No files changed'):
        run(tmp_path, client, apply=True)
    assert client.events == []
    report = json.loads((tmp_path / 'backup.json').read_text(encoding='utf-8'))
    assert 'source sync required' in report['conflicts'][0]


def test_rename_file_sends_name_and_metadata_to_scoped_endpoint(tmp_path):
    requests = []
    def handle(request):
        requests.append((request.method, request.url.path, json.loads(request.content)))
        return httpx.Response(403)
    http = httpx.AsyncClient(transport=httpx.MockTransport(handle), base_url='https://paratranz.cn/api/')
    client = ClientWrapper(http, 1, str(tmp_path))
    target = asyncio.run(Converter(client, None, Language.ko_KR).to_paratranz_file(FiletypeLang(
        'resources/BetterQuesting[cb4bq]/lang/en_US.lang', 'name=English\n',
    )))
    with pytest.raises(httpx.HTTPStatusError):
        asyncio.run(client.rename_file(17, target))
    assert requests == [('PUT', '/api/projects/1/files/17', {
        'name': CANONICAL, 'extra': target.file_extra.model_dump(),
    })]
