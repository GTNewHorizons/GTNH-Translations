from typing import Optional, TypeAlias, Any

from marshmallow import Schema, fields, post_load, post_dump, EXCLUDE


class JsonItemSchema(Schema):
    key = fields.String()
    original = fields.String()
    translation = fields.String(default="")
    context_ = fields.String(required=False, attribute="context", data_key="context")
    stage = fields.Integer(required=False)

    class Meta:
        unknown = EXCLUDE
        ordered = True

    @post_load
    def make_json_item(self, data: Any, **_: Any) -> "JsonItem":
        return JsonItem(**data)

    @post_dump
    def remove_none_values(self, data: Any, **_: Any) -> Any:
        return {k: v for k, v in data.items() if v is not None}


class JsonItem:
    def __init__(
        self,
        key: str,
        original: str,
        translation: str = "",
        context: Optional[str] = None,
        stage: Optional[int] = None,
    ):
        self.key = key
        self.original = original
        self.translation = translation
        self.context = context
        self.stage = stage


JsonItems: TypeAlias = list[JsonItem]
