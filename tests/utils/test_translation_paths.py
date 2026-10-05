import asyncio
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

from gtnh_translation_compare.paratranz.types import File, TranslationFile, StringItem
from gtnh_translation_compare.paratranz.converter import Converter
from gtnh_translation_compare.utils.translation_paths import merge_case_variants, remove_tracked_case_variants


LOWER = 'config/txloader/load/BetterQuesting[cb4bq]/lang/ko_KR.lang'
UPPER = LOWER.replace('[cb4bq]', '[CB4BQ]')


@pytest.mark.parametrize('reverse', [False, True])
def test_merge_keeps_translations_and_new_source_keys(reverse):
    files = [
        TranslationFile(relpath=UPPER, content='name=번역\n', translations={'lang|name': '번역'}),
        TranslationFile(relpath=LOWER, content='name=English\nnew=New key\n', translations={}),
    ]
    if reverse:
        files.reverse()
    merged, = merge_case_variants(files, {LOWER.casefold(): LOWER})
    assert merged.relpath == LOWER
    assert merged.content == 'name=번역\nnew=New key\n'
    assert files[0].content != merged.content


def test_merge_does_not_treat_old_english_as_a_translation():
    old = TranslationFile(relpath=UPPER, content='name=Old English\n', translations={})
    new = TranslationFile(relpath=LOWER, content='name=Current English\n', translations={})
    assert merge_case_variants([old, new], {})[0].content == new.content
    assert merge_case_variants([old], {LOWER.casefold(): LOWER})[0].relpath == LOWER


def test_merge_refuses_conflicting_or_missing_translated_keys():
    files = [
        TranslationFile(relpath=UPPER, content='name=A\n', translations={'lang|name': 'A'}),
        TranslationFile(relpath=LOWER, content='name=B\n', translations={'lang|name': 'B'}),
    ]
    with pytest.raises(ValueError, match='Conflicting translations'):
        merge_case_variants(files, {})
    files[1].content = 'other=English\n'
    files[1].translations = {}
    with pytest.raises(ValueError, match='missing from canonical'):
        merge_case_variants(files, {})


def test_tracked_alias_is_removed_before_canonical_write(tmp_path):
    subprocess.run(['git', 'init', '-q', str(tmp_path)], check=True)
    old = tmp_path / 'ko_KR' / UPPER
    old.parent.mkdir(parents=True)
    old.write_text('name=Old\n', encoding='utf-8')
    subprocess.run(['git', '-C', str(tmp_path), 'add', '.'], check=True)
    files = [TranslationFile(relpath=LOWER, content='name=번역\n', translations={'lang|name': '번역'})]
    remove_tracked_case_variants(tmp_path, Path('ko_KR'), files)
    target = tmp_path / 'ko_KR' / LOWER
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(files[0].content, encoding='utf-8')
    subprocess.run(['git', '-C', str(tmp_path), 'add', '--', 'ko_KR/' + LOWER], check=True)
    tracked = subprocess.check_output(['git', '-C', str(tmp_path), 'ls-files']).decode().splitlines()
    assert tracked == ['ko_KR/' + LOWER]
    assert target.read_text(encoding='utf-8') == files[0].content


def test_converter_refreshes_old_cache_and_records_real_translations():
    class Cache:
        def get(self, file):
            return TranslationFile(relpath=LOWER, content='stale')
        def set(self, file, value):
            self.value = value

    class Client:
        async def get_file(self, file_id):
            return File(id=file_id, name='resources/Test/lang/ko_KR.lang.json', extra={
                'original': 'name=English\n',
                'properties': {'lang|name': {'key': 'lang|name', 'start': 5, 'end': 12}},
                'en_us_relpath': 'resources/Test/lang/en_US.lang', 'target_relpath': LOWER,
            })
        async def get_strings(self, file_id):
            return [StringItem(key='lang|name', original='English', translation='번역')]

    cache = Cache()
    result = asyncio.run(Converter(Client(), cache, None).to_translation_file(File(id=1, name='test')))
    assert result.content == 'name=번역\n'
    assert result.translations == {'lang|name': '번역'}
    assert cache.value == result


@pytest.mark.parametrize('reverse', [False, True])
def test_removed_keys_warn_without_blocking_active_translations(monkeypatch, reverse):
    warnings = []
    monkeypatch.setattr('gtnh_translation_compare.utils.translation_paths.logger.warning',
                        lambda message, *args: warnings.append(message.format(*args)))
    files = [
        TranslationFile(relpath=UPPER, content='name=번역\nremoved=Old translation\n',
                        translations={'lang|name': '번역', 'lang|removed': 'Old translation'}),
        TranslationFile(relpath=LOWER, content='name=English\nnew=New key\n', translations={}),
        TranslationFile(relpath=UPPER.replace('[CB4BQ]', '[Cb4bq]'), content='removed=Different old translation\n',
                        translations={'lang|removed': 'Different old translation'}),
    ]
    if reverse:
        files.reverse()
    merged, = merge_case_variants(files, {LOWER.casefold(): LOWER},
                                 {LOWER.casefold(): {'lang|name', 'lang|new'}})
    assert merged.content == 'name=번역\nnew=New key\n'
    assert merged.translations == {'lang|name': '번역'}
    assert len(warnings) == 2
    assert all('lang|removed' in w and 'retained for review' in w for w in warnings)
    assert any('lang|removed' in f.translations for f in files)


def test_a_key_still_in_english_is_not_skipped_when_export_metadata_is_stale():
    files = [
        TranslationFile(relpath=UPPER, content='active=번역\n', translations={'lang|active': '번역'}),
        TranslationFile(relpath=LOWER, content='other=English\n', translations={}),
    ]
    with pytest.raises(ValueError, match='missing from canonical'):
        merge_case_variants(files, {LOWER.casefold(): LOWER},
                            {LOWER.casefold(): {'lang|active', 'lang|other'}})


def test_active_translation_conflicts_remain_errors():
    files = [
        TranslationFile(relpath=UPPER, content='name=A\n', translations={'lang|name': 'A'}),
        TranslationFile(relpath=LOWER, content='name=B\n', translations={'lang|name': 'B'}),
    ]
    with pytest.raises(ValueError, match='Conflicting translations'):
        merge_case_variants(files, {LOWER.casefold(): LOWER}, {LOWER.casefold(): {'lang|name'}})


def test_daily_lang_export_uses_current_english_keys_and_writes_other_files(tmp_path, monkeypatch):
    from gtnh_translation_compare.cmd.action import Action
    from gtnh_translation_compare.filetypes import Language

    subprocess.run(['git', 'init', '-q', str(tmp_path)], check=True)
    source = tmp_path / 'daily-history/resources/BetterQuesting[cb4bq]/lang/en_US.lang'
    source.parent.mkdir(parents=True)
    source.write_text('name=English\n', encoding='utf-8')
    monkeypatch.setattr('gtnh_translation_compare.cmd.action.settings.TARGET_LANG', Language.ko_KR)
    files = [
        TranslationFile(relpath=UPPER.replace('config/txloader/load/', 'resources/'),
                        content='name=번역\nremoved=Old translation\n',
                        translations={'lang|name': '번역', 'lang|removed': 'Old translation'}),
        TranslationFile(relpath=LOWER.replace('config/txloader/load/', 'resources/'),
                        content='name=English\n', translations={}),
        TranslationFile(relpath='resources/Other[other]/lang/ko_KR.lang',
                        content='other=Other translation\n', translations={'lang|other': 'Other translation'}),
    ]

    class Client:
        async def get_all_files(self):
            return [File(id=i, name=f.relpath + '.json') for i, f in enumerate(files)]

    class TestConverter:
        async def to_translation_file(self, file):
            return files[file.id].model_copy(deep=True)

    action = Action.__new__(Action)
    action.client = Client()
    action.converter = TestConverter()
    paths = asyncio.run(action._paratranz_to_lang(tmp_path, Path('ko_KR')))
    assert len(paths) == 2
    assert (tmp_path / 'ko_KR' / LOWER).read_text(encoding='utf-8') == 'name=번역\n'
    assert (tmp_path / 'ko_KR/config/txloader/load/Other[other]/lang/ko_KR.lang').read_text(encoding='utf-8') == 'other=Other translation\n'
    assert files[0].translations['lang|removed'] == 'Old translation'
