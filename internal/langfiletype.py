from .comparable import Comparable, Property


class LangFiletype(Comparable):
    def __init__(self, relpath: str, content: str):
        self.__relpath = relpath
        self.__content = content

    @property
    def relpath(self) -> str:
        return self.__relpath

    @property
    def content(self) -> str:
        return self.__content

    def get_properties(self, content: str) -> dict[str, Property]:
        properties: dict[str, Property] = {}
        end = 0
        for idx, line in enumerate(content.splitlines()):
            start = end + int(idx != 0)
            end = start + len(line)
            if line.startswith("#"):
                continue
            split = line.split("=", 1)
            if len(split) != 2:
                continue
            key = f"lang+{split[0]}"
            value = line
            properties[key] = Property(key, value, start, end)
        return properties

    def convert_relpath(self, relpath: str) -> str:
        return relpath.replace("en_US", "zh_CN")
