import json
import os
import re
from os import path
from typing import List, Dict, Set, Tuple, Sequence

from . import Comparable
from .comparable import Property

EN_DUPLICATE_KEYS: Dict[str, Set[str]] = {}
ZH_DUPLICATE_KEYS: Dict[str, Set[str]] = {}

with open("hooks.json") as hooks_fp:
    hooks = json.load(hooks_fp)
insert_hooks = hooks.get("insert", [])
replace_hooks = hooks.get("replace", [])


def generate_translation(
    old_files: Sequence[Comparable],
    new_files: Sequence[Comparable],
    ref_files: Sequence[Comparable],
    output_path: str,
):
    old_properties = collect_properties(old_files, "en")
    ref_properties = collect_properties(ref_files, "zh")
    value_to_first_key_dict = get_value_to_first_key_dict(old_properties)

    for new_file in new_files:
        output_file_path = path.join(output_path, new_file.converted_relpath)
        os.makedirs(path.dirname(output_file_path), exist_ok=True)
        content = new_file.content
        properties: List[Tuple[str, Property]] = [(k, v) for k, v in new_file.properties.items()]

        def sort_key(item: Tuple[str, Property]):
            _, p = item
            return p.start

        properties.sort(key=sort_key, reverse=True)

        for k, v in properties:
            if k in old_properties:
                if old_properties[k].value == v.value:
                    if k in ref_properties:
                        content = content[: v.start] + ref_properties[k].value + content[v.end :]
                else:
                    if k in ref_properties:
                        content = (
                            content[: v.start]
                            + mark_diff(
                                old_properties.get(k) and old_properties.get(k).value or "",
                                v.value,
                                ref_properties.get(k) and ref_properties.get(k).value or "",
                            )
                            + content[v.end :]
                        )
            elif v.value in value_to_first_key_dict:
                first_key = value_to_first_key_dict[v.value]
                if first_key in ref_properties:
                    content = (
                        content[: v.start]
                        + mark_new_with_same_value(v.value, ref_properties[first_key].value)
                        + content[v.end :]
                    )
            else:
                content = content[: v.start] + mark_new(v.value) + content[v.end :]

        content = apply_hooks(new_file.converted_relpath, content)
        with open(output_file_path, "w", encoding="utf-8") as fp:
            fp.write(content)


def apply_hooks(relpath: str, content: str) -> str:
    for h in replace_hooks:
        if re.search(h["path_match"], relpath):
            content = content.replace(h["old"], h["new"])
    for h in insert_hooks:
        if re.search(h["path_match"], relpath):
            content = h["content"] + content

    return content


def collect_properties(files: Sequence[Comparable], _type: str):
    properties: Dict[str, Property] = {}
    for file in files:
        for k, v in file.properties.items():
            if k in properties:
                add_duplicate_key(k, v.value, _type)
                add_duplicate_key(k, properties[k].value, _type)
            properties[k] = v
    return properties


def get_value_to_first_key_dict(properties: Dict[str, Property]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for k, v in properties.items():
        result[v.value] = k
    return result


def add_duplicate_key(k: str, v: str, _type: str):
    if _type == "en":
        dk = EN_DUPLICATE_KEYS
    else:
        dk = ZH_DUPLICATE_KEYS
    if k not in dk:
        dk[k] = set()
    dk[k].add(v)


def mark(s: str, content: str):
    return "\n".join([f"// {s * 3} //{line}" for line in content.splitlines()])


def mark_diff(old_en: str, new_en: str, old_zh: str):
    return f"{mark('-', old_zh)}\n{mark('+', new_en)}\n{mark('↑', old_en)}"


def mark_new(new_en: str):
    return mark("+", new_en)


def mark_duplicate(en: str):
    return mark("x", en)


def mark_new_with_same_value(new_en: str, new_zh: str):
    return f"{mark('+', new_zh)}\n{mark('↑', new_en)}"
