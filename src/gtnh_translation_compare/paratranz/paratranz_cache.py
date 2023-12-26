import base64
import os

from gtnh_translation_compare.paratranz.types import File, TranslationFile


class ParatranzCache:
    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    @staticmethod
    def _calc_cache_name(f: File) -> str:
        return base64.urlsafe_b64encode(f"{f.name} + {f.modified_at}".encode()).decode()

    # noinspection PyBroadException
    def get(self, f: File) -> TranslationFile | None:
        try:
            filepath = os.path.join(self.cache_dir, self._calc_cache_name(f))
            with open(filepath, "r") as fp:
                result = TranslationFile.model_validate_json(fp.read())
                # update file modified time when valid cache found
                os.utime(filepath)
                return result
        except Exception:
            return None

    def set(self, f: File, translation_file: TranslationFile) -> None:
        filepath = os.path.join(self.cache_dir, self._calc_cache_name(f))
        with open(filepath, "w") as fp:
            fp.write(translation_file.model_dump_json())
