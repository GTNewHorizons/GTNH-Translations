from abc import ABCMeta, abstractmethod
from typing import Dict


class Comparable(metaclass=ABCMeta):
    @property
    @abstractmethod
    def relpath(self) -> str:
        pass

    @property
    @abstractmethod
    def content(self) -> str:
        pass

    @property
    def properties(self) -> Dict[str, str]:
        return self.get_properties(self.content)

    @property
    def converted_relpath(self) -> str:
        return self.convert_relpath(self.relpath)

    @abstractmethod
    def get_properties(self, content: str) -> Dict[str, str]:
        pass

    def convert_relpath(self, relpath: str) -> str:
        return relpath
