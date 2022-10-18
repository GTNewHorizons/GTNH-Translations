from typing import Any, TypeAlias

from marshmallow import Schema, fields, post_load


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
    zh_cn_relpath = fields.String()

    @post_load
    def to_file_extra(self, data: Any, **_: Any) -> "FileExtra":
        return FileExtra(**data)


class FileExtra:
    def __init__(self, original: str, properties: Properties, en_us_relpath: str, zh_cn_relpath: str):
        self.original = original
        self.properties = properties
        self.en_us_relpath = en_us_relpath
        self.zh_cn_relpath = zh_cn_relpath
