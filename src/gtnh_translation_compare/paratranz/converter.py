import io
from dataclasses import dataclass
from os import path
from typing import BinaryIO
from io import StringIO

from paratranz_client.models.file import File
from paratranz_client.models.string_item import StringItem
from paratranz_client.types import File as FileToBeUploaded

from gtnh_translation_compare.filetypes import Language
from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.paratranz.file_extra import FileExtra, FileExtraSchema, Properties, Property
from gtnh_translation_compare.paratranz.json_item import (
    JsonItems,
    JsonItem,
    JsonItemSchema,
)
from gtnh_translation_compare.utils.unicode import to_unicode
from loguru import logger


@dataclass
class ParatranzFile:
    file_model: File
    file_model_extra: FileExtra
    json_items: JsonItems

    @property
    def binary_json(self) -> BinaryIO:
        return io.BytesIO(JsonItemSchema().dumps(self.json_items, many=True).encode())

    @property
    def file(self) -> FileToBeUploaded:
        assert isinstance(self.file_model.name, str)
        return FileToBeUploaded(
            payload=self.binary_json,
            file_name=path.basename(self.file_model.name),
            mime_type="application/json",
        )


def to_paratranz_file(
    file: Filetype,
) -> ParatranzFile:
    paratranz_file = File()
    paratranz_file.name = file.get_target_language_relpath(Language.zh_CN) + ".json"
    json_content: JsonItems = [JsonItem(key=p.key, original=p.value, context=p.full) for p in file.properties.values()]
    paratranz_file_extra_properties: Properties = {
        k: Property(key=p.key, start=p.start, end=p.end) for k, p in file.properties.items()
    }
    paratranz_file_extra = FileExtra(
        original=file.content,
        properties=paratranz_file_extra_properties,
        en_us_relpath=file.get_en_us_relpath(),
        target_relpath=file.get_target_language_relpath(Language.zh_CN),
    )
    logger.info("to_paratranz_file: {}", paratranz_file.name)
    return ParatranzFile(paratranz_file, paratranz_file_extra, json_content)


@dataclass
class TranslationFile:
    relpath: str
    content: str


def sort_key(item: tuple[str, Property]) -> int:
    _, p = item
    return p.start


def to_translation_file(paratranz_file: File, paratranz_file_strings: list[StringItem]) -> TranslationFile:
    file_extra_dict = paratranz_file.additional_properties["extra"]
    file_extra: FileExtra = FileExtraSchema().load(file_extra_dict)
    content = file_extra.original
    json_items: JsonItems = [JsonItemSchema().load(string.to_dict()) for string in paratranz_file_strings]
    json_items_map: dict[str, JsonItem] = {item.key: item for item in json_items}

    properties: list[tuple[str, Property]] = [(k, v) for k, v in file_extra.properties.items()]
    properties.sort(key=sort_key)

    is_script = file_extra.target_relpath.startswith("scripts/")

    left = 0
    buffer = StringIO()
    for k, p in properties:
        if k not in json_items_map:
            continue
        json_item: JsonItem = json_items_map[k]
        translation = json_item.translation
        if translation:
            if is_script:
                translation = "<BR>".join([to_unicode(p) for p in translation.split("<BR>")])
            buffer.write(content[left : p.start])
            buffer.write(translation)
        else:
            buffer.write(content[left : p.end])
        left = p.end
    buffer.write(content[left:])

    translated_content = buffer.getvalue()
    if is_script:
        translated_content = translated_content.replace('val _I18N_Lang = "en_US";', 'val _I18N_Lang = "zh_CN";')
    logger.info("to_translation_file: {}", file_extra.target_relpath)
    return TranslationFile(file_extra.target_relpath, translated_content)
