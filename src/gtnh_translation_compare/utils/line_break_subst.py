import re
from typing import Optional

from loguru import logger

from gtnh_translation_compare import settings
from gtnh_translation_compare.paratranz.types import File

LINE_BREAK_CONTEXT_PREFIX = "@gtnh-line-break-form="
LINE_BREAK_CONTEXT_NOOP = "LF"
LINE_BREAK_CONTEXT_DECODE_MAP = {
  "<br>-UP": "<BR>",
  "<br>": "<br>",
  "[br]": "[br]",
  "\\\\n": "\\\\n",
  "\\n": "\\n",
  "%n": "%n",
}


def get_line_break_symbol(dflt_setting: Optional[str], context: Optional[str]) -> str:
  if dflt_setting is None:
    default_symbol = LINE_BREAK_CONTEXT_NOOP
  else:
    default_symbol = dflt_setting
  if context is None: return default_symbol
  sp_ctx: list[str] = re.split(r'\r?\n', context)
  for ctx_line in sp_ctx:
    if not ctx_line.startswith(LINE_BREAK_CONTEXT_PREFIX): continue
    norm_to_entry = ctx_line[len(LINE_BREAK_CONTEXT_PREFIX):]
    if norm_to_entry == LINE_BREAK_CONTEXT_NOOP: return norm_to_entry
    if norm_to_entry not in LINE_BREAK_CONTEXT_DECODE_MAP:
      logger.warning(f"Not recognized for line break: {norm_to_entry}")
      return default_symbol
    return LINE_BREAK_CONTEXT_DECODE_MAP[norm_to_entry]
  return default_symbol


def line_break_subst(file: File, context: Optional[str], translation: str) -> str:
  dflt_sym = None
  if file.name == settings.GT_LANG_TARGET_REL_PATH + ".json":
    dflt_sym = "<BR>"
  sym = get_line_break_symbol(dflt_sym, context)
  if sym == LINE_BREAK_CONTEXT_NOOP: return translation
  return re.sub(r'\r?\n', lambda m: sym, translation)
