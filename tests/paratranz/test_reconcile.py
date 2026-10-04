import asyncio
import json
from pathlib import Path

import httpx
import pytest

from gtnh_translation_compare.filetypes import Language
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

    async def get_strings(self, file_id):
        return [s.model_copy(deep=True) for s in self.strings[file_id]]

    async def upload_file(self, target):
        self.events.append('upload')
        self.files[2] = File(id=2, name=target.file_name)
        self.strings[2] = [s.model_copy(deep=True) for s in target.string_items]
        if self.fail_verification:
            self.strings[2][0].translation = ''
        return 2

    async def delete_file(self, file_id):
        self.events.append('delete')
        assert self.strings[2][0].translation == '번역'
        assert self.strings[2][0].stage == 5
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
    assert client.events == ['upload', 'delete']
    assert list(client.files) == [2]


def test_failed_readback_never_deletes_alias(tmp_path):
    client = Client(fail_verification=True)
    with pytest.raises(ValueError, match='verification failed'):
        run(tmp_path, client, apply=True)
    assert client.events == ['upload']
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
        async def get_strings(self, file_id):
            strings = await super().get_strings(file_id)
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
