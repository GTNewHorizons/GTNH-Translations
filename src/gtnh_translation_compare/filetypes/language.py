from enum import Enum
from typing import List


class Language(Enum):
    en_US = "en_US"
    zh_CN = "zh_CN"
    ja_JP = "ja_JP"
    ko_KR = "ko_KR"
    pt_BR = "pt_BR"
    fr_FR = "fr_FR"
    es_ES = "es_ES"
    tr_TR = "tr_TR"
    de_DE = "de_DE"
    pl_PL = "pl_PL"

    @classmethod
    def from_str(cls, s: str) -> "Language":
        return cls(s)

    @classmethod
    def values(cls) -> List[str]:
        return [_.value for _ in cls.__members__.values()]

    @classmethod
    def values_except_en_us(cls) -> List[str]:
        return [_.value for _ in cls.__members__.values() if _ != cls.en_US]
