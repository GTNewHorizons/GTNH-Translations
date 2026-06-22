import re
from typing import Optional

from loguru import logger

LINE_BREAK_CONTEXT_PREFIX = "@gtnh-line-break-form="
LINE_BREAK_CONTEXT_NOOP = "LF"
LINE_BREAK_CONTEXT_DECODE_MAP = {
  "<BR>-UP": "<BR>",
  "<BR>": "<br>",
  "[br]": "[br]",
  "\\\\n": "\\\\n",
  "\\n": "\\n",
  "%n": "%n",
}


def line_break_subst(context: Optional[str], translation: str) -> str:
  if context is None: return translation
  sp_ctx: list[str] = re.split(r'\r?\n', context)
  for ctx_line in sp_ctx:
    if not ctx_line.startswith(LINE_BREAK_CONTEXT_PREFIX): continue
    norm_to_entry = ctx_line[len(LINE_BREAK_CONTEXT_PREFIX):]
    if norm_to_entry == LINE_BREAK_CONTEXT_NOOP: return translation
    if norm_to_entry not in LINE_BREAK_CONTEXT_DECODE_MAP:
      logger.warning(f"Not recognized for line break: {norm_to_entry}")
      return translation
    norm_to = LINE_BREAK_CONTEXT_DECODE_MAP[norm_to_entry]
    return re.sub(r'\r?\n', norm_to, translation)
  return translation
