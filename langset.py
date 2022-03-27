from utils import match_lang_line


class LangSet:
    def __init__(self, lang_files: dict[str, str]):
        self.__lang_files = lang_files
        self.__lang_key_to_value_map: dict[str, str] = {}
        self.__lang_key_to_relpath_map: dict[str, str] = {}
        self.__generate_maps()

    def __generate_maps(self):
        for rel_path, content in self.__lang_files.items():
            for line in content.splitlines():
                k, v = match_lang_line(line)
                if k is not None:
                    self.__lang_key_to_value_map[k] = v
                    self.__lang_key_to_relpath_map[k] = rel_path

    def get_lang_file_relpath_list(self) -> list[str]:
        return list(self.__lang_files.keys())

    def get_keys(self) -> list[str]:
        return list(self.__lang_key_to_value_map.keys())

    def get_relpath_by_key(self, key: str, default=None) -> str:
        return self.__lang_key_to_relpath_map.get(key, default)

    def get_value(self, key: str, default=None) -> str:
        return self.__lang_key_to_value_map.get(key, default)

    def get_content(self, relpath: str, default=None) -> str:
        return self.__lang_files.get(relpath, default)
