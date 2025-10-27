from io import StringIO
from typing import List, Tuple, Dict

from loguru import logger

from gtnh_translation_compare.filetypes import Language
from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.filetypes.linebreak import linebreak_restorer, linebreak_normalizer
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.paratranz_cache import ParatranzCache
from gtnh_translation_compare.paratranz.types import (
    ParatranzFile,
    TranslationFile,
    File,
    FileExtra,
    Property,
    StringItem,
)
from gtnh_translation_compare.utils.unicode import to_unicode


class Converter:
    def __init__(self, client: ClientWrapper, cache: ParatranzCache, target_lang: Language):
        self.client = client
        self.cache = cache
        self.target_lang = target_lang

    async def to_translation_file(self, paratranz_file: File) -> "TranslationFile":
        cached = self.cache.get(paratranz_file)
        if cached:
            logger.info("cache hit: {}", paratranz_file.name)
            return cached
        translation_file = await self._to_translation_file(paratranz_file)
        self.cache.set(paratranz_file, translation_file)
        logger.info("cache miss: {}", paratranz_file.name)
        return translation_file

    async def _to_translation_file(self, paratranz_file: File) -> "TranslationFile":
        paratranz_file = await self.client.get_file(paratranz_file.id)
        file_extra_dict = paratranz_file.extra
        file_extra = FileExtra.model_validate(file_extra_dict)
        content = file_extra.original
        string_items = await self.client.get_strings(paratranz_file.id)
        string_items_map = {item.key: item for item in string_items}
        linebreak_mapper = linebreak_restorer(file_extra.en_us_relpath)

        properties: List[Tuple[str, Property]] = [(k, v) for k, v in file_extra.properties.items()]
        properties.sort(key=sort_key)

        left = 0
        buffer = StringIO()
        for k, p in properties:
            if k not in string_items_map:
                continue
            string_item = string_items_map[k]
            translation = linebreak_mapper(string_item.translation)
            if translation:
                buffer.write(content[left : p.start])
                buffer.write(translation)
            else:
                buffer.write(content[left : p.end])
            left = p.end
        buffer.write(content[left:])

        translated_content = buffer.getvalue()
        return TranslationFile(relpath=file_extra.target_relpath, content=translated_content)

    async def to_paratranz_file(self, file: Filetype) -> "ParatranzFile":
        file_name = file.get_target_language_relpath(self.target_lang) + ".json"
        linebreak_mapper = linebreak_normalizer(file.get_en_us_relpath())
        string_list: List[StringItem] = [
            StringItem(key=p.key, original=linebreak_mapper(p.value), context=p.full) for p in file.properties.values()  # pyright: ignore [reportCallIssue]
        ]
        paratranz_file_extra_properties: Dict[str, Property] = {
            k: Property(key=p.key, start=p.start, end=p.end) for k, p in file.properties.items()
        }
        paratranz_file_extra = FileExtra(
            original=file.content,
            properties=paratranz_file_extra_properties,
            en_us_relpath=file.get_en_us_relpath(),
            target_relpath=file.get_target_language_relpath(self.target_lang),
        )
        logger.info(file_name)
        return ParatranzFile(
            file_name=file_name,
            file_extra=paratranz_file_extra,
            string_items=string_list,
        )


def sort_key(item: tuple[str, Property]) -> int:
    _, p = item
    return p.start
