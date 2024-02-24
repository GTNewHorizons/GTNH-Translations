import json
import os
from typing import Dict, Any, Optional, TypeAlias, List, Tuple

from loguru import logger
from pydantic import BaseModel as BaseModel, Field, model_validator, AliasChoices

from gtnh_translation_compare.filetypes import Language

# [file_name, file_content, mime_type]
FileToBeUploaded: TypeAlias = Tuple[str, str, str]


class File(BaseModel):
    id: int
    modified_at: Optional[str] = Field(None, validation_alias=AliasChoices("modifiedAt", "modified_at"))
    name: str
    extra: Optional[Dict[str, Any]] = Field(None)


class StringItem(BaseModel):
    id: Optional[int] = Field(None)
    key: str
    original: str
    translation: str = Field("")
    context: Optional[str] = Field(None)
    stage: Optional[int] = Field(None)


StringList: TypeAlias = List[StringItem]


class StringPage(BaseModel):
    page_count: int = Field(validation_alias=AliasChoices("pageCount", "page_count"))
    results: StringList


###
class Property(BaseModel):
    key: str
    start: int
    end: int


class FileExtra(BaseModel):
    original: str
    properties: Dict[str, Property]
    en_us_relpath: str
    target_relpath: str

    # noinspection PyNestedDecorators
    @model_validator(mode="before")
    @classmethod
    def check_legacy(cls, data: Any) -> Any:
        if isinstance(data, dict):
            for lang in Language.__members__.values():
                if f"{lang.value}_relpath" in data:
                    data["target_relpath"] = data[f"{lang.value}_relpath"]
                    data.pop(f"{lang.value}_relpath")
                    logger.warning(
                        f"FileExtra.{lang.value}_relpath is deprecated, use FileExtra.target_relpath instead"
                    )
        return data


class ParatranzFile(BaseModel):
    file_name: str
    file_extra: FileExtra
    string_items: StringList

    @property
    def file_to_be_uploaded(self) -> FileToBeUploaded:
        return (
            os.path.basename(self.file_name),
            json.dumps([s.model_dump(exclude_none=True) for s in self.string_items]),
            "application/json",
        )


class TranslationFile(BaseModel):
    relpath: str
    content: str
