from abc import ABCMeta, abstractmethod
from typing import Dict, final, TYPE_CHECKING

from gtnh_translation_compare.filetypes.property import Property

if TYPE_CHECKING:
    from gtnh_translation_compare.filetypes import Language


class Filetype(metaclass=ABCMeta):
    @property
    @final
    def relpath(self) -> str:
        return self._get_relpath()

    @abstractmethod
    def _get_relpath(self) -> str:
        pass

    @property
    @final
    def content(self) -> str:
        return self._get_content()

    @abstractmethod
    def _get_content(self) -> str:
        pass

    @property
    @final
    def properties(self) -> Dict[str, Property]:
        return self._get_properties(self.content)

    @abstractmethod
    def _get_properties(self, content: str) -> Dict[str, Property]:
        pass

    @abstractmethod
    def get_en_us_relpath(self) -> str:
        pass

    @abstractmethod
    def get_target_language_relpath(self, target_language: "Language") -> str:
        pass
