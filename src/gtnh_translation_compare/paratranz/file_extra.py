from typing import Any, TypeAlias

from marshmallow import Schema, fields, post_load

from loguru import logger


class PropertySchema(Schema):
    key = fields.String()
    start = fields.Integer()
    end = fields.Integer()

    @post_load
    def make_property(self, data: Any, **_: Any) -> "Property":
        return Property(**data)


class Property:
    def __init__(self, key: str, start: int, end: int):
        self.key = key
        self.start = start
        self.end = end


Properties: TypeAlias = dict[str, Property]


class FileExtraSchema(Schema):
    original = fields.String()
    properties = fields.Dict(fields.String(), fields.Nested(PropertySchema()))
    en_us_relpath = fields.String()
    target_relpath = fields.String(required=False)
    # Deprecated
    zh_cn_relpath = fields.String(required=False)
    # Deprecated
    ja_jp_relpath = fields.String(required=False)

    @post_load
    def to_file_extra(self, data: Any, **_: Any) -> "FileExtra":
        # Legacy
        if "zh_cn_relpath" in data:
            logger.warning("FileExtra.zh_cn_relpath is deprecated, use FileExtra.target_relpath instead")
            data["target_relpath"] = data["zh_cn_relpath"]
            data.pop("zh_cn_relpath")
        if "ja_jp_relpath" in data:
            logger.warning("FileExtra.ja_jp_relpath is deprecated, use FileExtra.target_relpath instead")
            data["target_relpath"] = data["ja_jp_relpath"]
            data.pop("ja_jp_relpath")
        return FileExtra(**data)


class FileExtra:
    def __init__(self, original: str, properties: Properties, en_us_relpath: str, target_relpath: str):
        self.original = original
        self.properties = properties
        self.en_us_relpath = en_us_relpath
        self.target_relpath = target_relpath
