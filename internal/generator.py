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


def add_duplicate_key(k: str, v: str, _type: str):
    if _type == "en":
        dk = EN_DUPLICATE_KEYS
    else:
        dk = ZH_DUPLICATE_KEYS
    if k not in dk:
        dk[k] = set()
    dk[k].add(v)


def mark_diff(old_en: str, new_en: str, old_zh: str):
    old_zh = "\n".join([f"// --- //{line}" for line in old_zh.splitlines()])
    new_en = "\n".join([f"// +++ //{line}" for line in new_en.splitlines()])
    old_en = "\n".join([f"// ↑↑↑ //{line}" for line in old_en.splitlines()])
    return f"{old_zh}\n{new_en}\n{old_en}"


def mark_new(new_en: str):
    return "\n".join([f"// +++ //{line}" for line in new_en.splitlines()])


def mark_duplicate(en: str):
    return "\n".join([f"// xxx //{line}" for line in en.splitlines()])
