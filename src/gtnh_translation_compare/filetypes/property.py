from dataclasses import dataclass


# noinspection PyUnresolvedReferences
@dataclass
class Property:
    """
    Indicates an entry in a localization file

    Attributes:
        key (str): The unique identifier of the entry
        value (str): The full content of the entry
        start (int): The start position of the entry in the file
        end (int): The end position of the entry in the file
    """

    key: str
    value: str
    start: int
    end: int
