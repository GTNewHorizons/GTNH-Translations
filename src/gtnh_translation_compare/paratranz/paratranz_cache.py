import os
import base64
import pickle

from gtnh_translation_compare.paratranz.converter import TranslationFile
from gtnh_translation_compare.paratranz.paratranz_file_ref import ParatranzFileRef


class ParatranzCache:
    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir

    @staticmethod
    def _calc_cache_name(paratranz_file_ref: ParatranzFileRef) -> str:
        return base64.urlsafe_b64encode(
            f"{paratranz_file_ref.value.name} + {paratranz_file_ref.value.modified_at.timestamp()}".encode()
        ).decode()

    # noinspection PyBroadException
    def get(self, paratranz_file_ref: ParatranzFileRef) -> TranslationFile | None:
        try:
            filepath = os.path.join(self.cache_dir, self._calc_cache_name(paratranz_file_ref))
            with open(filepath, "rb") as fp:
                return pickle.load(fp)
        except Exception:
            return None

    def set(self, paratranz_file_ref: ParatranzFileRef, translation_file: TranslationFile) -> None:
        filepath = os.path.join(self.cache_dir, self._calc_cache_name(paratranz_file_ref))
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "wb") as fp:
            pickle.dump(translation_file, fp)
