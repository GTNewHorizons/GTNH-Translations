from abc import ABCMeta, abstractmethod
from typing import Dict


class Property:
    def __init__(self, key: str, value: str, start: int, end: int):
        self.key = key
        self.value = value
        self.start = start
        self.end = end


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
    def properties(self) -> Dict[str, Property]:
        return self.get_properties(self.content)

    @property
    def converted_relpath(self) -> str:
        return self.convert_relpath(self.relpath)

    @abstractmethod
    def get_properties(self, content: str) -> Dict[str, Property]:
        pass

    def convert_relpath(self, relpath: str) -> str:
        return relpath
