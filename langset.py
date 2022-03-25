import re

LANG_LINE_PATTERN = re.compile(r'^([^/#]+?)=(.*)$')


class LangSet:
    def __init__(self):
        self.__lang_key_value_map = None
        self.__lang_key_file_map = None

    @property
    def lang_map(self):
        raise NotImplementedError()

    @property
    def lang_key_value_map(self):
        if self.__lang_key_value_map is None:
            self.__generate_key_related_maps()
        return self.__lang_key_value_map

    @property
    def lang_key_file_map(self):
        if self.__lang_key_file_map is None:
            self.__generate_key_related_maps()
        return self.__lang_key_file_map

    def __generate_key_related_maps(self):
        self.__lang_key_value_map = {}
        self.__lang_key_file_map = {}
        for filename, content in self.lang_map.items():
            for line in content.splitlines():
                match = LANG_LINE_PATTERN.match(line)
                if match:
                    self.__lang_key_value_map[match.group(1)] = match.group(2)
                    self.__lang_key_file_map[match.group(1)] = filename
