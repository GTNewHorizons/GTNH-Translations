import re
from typing import Dict

from gtnh_translation_compare.filetypes.filetype import Filetype
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property

# Shared between modpack.py's guide pack scanner, the daily-sync workflow's changed-file
# dispatcher, and the ParaTranz-download filter, so all three agree on what counts as a
# GuideNH page. Language-agnostic (matches any locale segment) since callers see the file
# under different locales depending on which side they're on.
GUIDENH_PAGE_PATH_RE = re.compile(r"/guidenh/_[a-z]{2}_[a-z]{2}/.*\.md$")


def is_guidenh_page_path(relpath: str) -> bool:
    return GUIDENH_PAGE_PATH_RE.search(relpath) is not None


def is_guidenh_page_paratranz_file(name: str) -> bool:
    # ParaTranz always appends ".json" to the original file's relpath.
    return is_guidenh_page_path(name.removesuffix(".json"))


def language_folder(language: Language) -> str:
    # GuideNH reads locale folders in the underscored lowercase form ("_en_us"), while
    # Language carries the Minecraft form ("en_US").
    return f"_{language.value.lower()}"


class FiletypeGuideNhPage(Filetype):
    """
    A GuideNH guide page (`assets/<namespace>/guidenh/_<locale>/<page>.md`), shipped in the
    GTNH Guide Pack and loaded from `config/guidenh/DefaultGuide.zip`. Like the GregTech
    markdown tooltips, there is no key=value structure: the whole file is markdown with YAML
    frontmatter, addressed by its file path rather than by a key inside it.

    We therefore treat the entire file as a single translatable unit, keyed by its own
    relpath, which lets translators reflow a full page as one coherent text.
    """

    def __init__(self, relpath: str, content: str, language: Language = Language.en_US):
        self._relpath = relpath
        self._content = content
        self._language = language

    def _get_relpath(self) -> str:
        return self._relpath

    def _get_content(self) -> str:
        return self._content

    def _get_properties(self, content: str) -> Dict[str, Property]:
        if content == "":
            return {}
        # The key must be language-independent: ParaTranz stores it built from the en_US path, so a
        # translated file has to produce the same key for its content to be matched against it.
        key = f"guidenh-page|{self.get_en_us_relpath()}"
        return {key: Property(key=key, value=content, full=content, start=0, end=len(content))}

    def get_en_us_relpath(self) -> str:
        if self._language == Language.en_US:
            return self._relpath
        return self._relpath.replace(language_folder(self._language), language_folder(Language.en_US))

    def get_target_language_relpath(self, target_language: Language) -> str:
        if self._language == target_language:
            return self._relpath
        return self._relpath.replace(language_folder(self._language), language_folder(target_language))
