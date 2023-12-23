import os
from pathlib import Path
from typing import TypeAlias, Callable, Optional

import requests
from dulwich import porcelain
from paratranz_client.client import AuthenticatedClient

from gtnh_translation_compare import settings
from gtnh_translation_compare.filetypes import FiletypeLang, Language, FiletypeGTLang
from gtnh_translation_compare.modpack.modpack import ModPack
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import TranslationFile, to_translation_file, to_paratranz_file
from gtnh_translation_compare.utils.file import ensure_lf

ParatranzFilenameFilter: TypeAlias = Callable[[str], bool]
AfterToTranslationFileCallback: TypeAlias = Callable[[TranslationFile], None]


class Action:
    def __init__(self) -> None:
        paratranz_project_id = settings.PARATRANZ_PROJECT_ID
        paratranz_token = settings.PARATRANZ_TOKEN
        client = AuthenticatedClient(
            base_url="https://paratranz.cn/api",
            token=paratranz_token,
            verify_ssl=False,
            timeout=1000,
            headers={"Authorization": paratranz_token},
        )
        self.client = ClientWrapper(client, paratranz_project_id)

    @staticmethod
    def __commit(repo: str, paths: list[str], message: str, issue: object) -> None:
        porcelain.add(repo, paths)  # type: ignore[no-untyped-call]
        commit_message = message
        if issue is not None and settings.CLOSE_ISSUE_IN_COMMIT_MESSAGE:
            commit_message += f"\n\nclosed #{issue}"
        porcelain.commit(  # type: ignore[no-untyped-call]
            repo,
            message=commit_message,
            author=settings.GIT_AUTHOR,
        )

    @staticmethod
    def __write(filepath: str, content: str) -> None:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as fp:
            fp.write(content)

    @staticmethod
    def __write_translation_file(filepath: str, translation_file: TranslationFile) -> None:
        Action.__write(filepath, translation_file.content)

    def __paratranz_to_translation(
        self,
        filter_: ParatranzFilenameFilter,
        after_to_translation_file_callback: Optional[AfterToTranslationFileCallback],
        raise_when_empty: Optional[Exception],
        message: str,
        repo_path: Optional[str] = None,
        issue: Optional[str] = None,
    ) -> None:
        translation_files: list[TranslationFile] = []
        translation_filepaths: list[str] = []
        for f in self.client.all_files:
            if filter_(f.name):
                strings = self.client.get_strings(f.id)
                translation_file = to_translation_file(f, strings)
                if after_to_translation_file_callback is not None:
                    after_to_translation_file_callback(translation_file)
                translation_files.append(translation_file)

        if len(translation_files) == 0:
            if raise_when_empty is not None:
                raise raise_when_empty

        if repo_path is None:
            for translation_file in translation_files:
                print(translation_file.content)
            return

        for translation_file in translation_files:
            translation_filepath = os.path.abspath(os.path.join(repo_path, translation_file.relpath))
            translation_filepaths.append(translation_filepath)
            self.__write_translation_file(translation_filepath, translation_file)

        self.__commit(
            repo_path,
            translation_filepaths,
            message,
            issue,
        )

    # region Quest Book
    def quest_book_to_paratranz(self, commit_sha: Optional[str] = None) -> None:
        if commit_sha is None or commit_sha == "":
            commit_sha = "master"
        qb_lang_file_url = f"https://raw.githubusercontent.com/{settings.GTNH_REPO}/{commit_sha}/{settings.DEFAULT_QUESTS_LANG_TEMPLATE_REL_PATH}"
        res = requests.get(qb_lang_file_url)
        if res.status_code != 200:
            raise ValueError(f"Failed to get quest book file from {qb_lang_file_url}")
        qb_lang_file = FiletypeLang(
            relpath=settings.DEFAULT_QUESTS_LANG_TARGET_REL_PATH, content=res.text, language=Language.en_US
        )
        qb_paratranz_file = to_paratranz_file(qb_lang_file)
        self.client.upload_file(qb_paratranz_file)

    def paratranz_to_quest_book(self, repo_path: Optional[str] = None, issue: Optional[str] = None) -> None:
        filter_: ParatranzFilenameFilter = lambda name: name == settings.DEFAULT_QUESTS_LANG_TARGET_REL_PATH + ".json"
        self.__paratranz_to_translation(
            filter_,
            None,
            ValueError("No quest book file found"),
            "[自动化] 更新 任务书",
            repo_path,
            issue,
        )

    # endregion Quest Book

    # region Lang + Zs
    def lang_and_zs_to_paratranz(self, modpack_path: str) -> None:
        modpack = ModPack(Path(modpack_path))
        for lang_file in modpack.lang_files:
            lang_paratranz_file = to_paratranz_file(lang_file)
            self.client.upload_file(lang_paratranz_file)
        for script_file in modpack.script_files:
            script_paratranz_file = to_paratranz_file(script_file)
            self.client.upload_file(script_paratranz_file)

    def paratranz_to_lang_and_zs(self, repo_path: Optional[str] = None, issue: Optional[str] = None) -> None:
        def filter_(name: str) -> bool:
            return any(
                [
                    name.endswith(".lang" + ".json")
                    and name != settings.DEFAULT_QUESTS_LANG_TARGET_REL_PATH + ".json"
                    and name != settings.GT_LANG_TARGET_REL_PATH + ".json",
                    name.endswith(".zs" + ".json"),
                ]
            )

        self.__paratranz_to_translation(
            filter_,
            None,
            ValueError("No lang or zs file found"),
            "[自动化] 更新 语言文件 + 脚本",
            repo_path,
            issue,
        )

    # endregion Lang + Zs

    # region Gt Lang
    def gt_lang_to_paratranz(self, gt_lang_url: str) -> None:
        res = requests.get(gt_lang_url)
        gt_lang_file = FiletypeGTLang(
            relpath=settings.GT_LANG_TARGET_REL_PATH,
            content=ensure_lf(res.text),
            language=Language.en_US,
        )
        gt_paratranz_file = to_paratranz_file(gt_lang_file)
        self.client.upload_file(gt_paratranz_file)

    def paratranz_to_gt_lang(self, repo_path: Optional[str] = None, issue: Optional[str] = None) -> None:
        filter_: ParatranzFilenameFilter = lambda name: name == settings.GT_LANG_TARGET_REL_PATH + ".json"

        def after_to_translation_file_callback(translation_file: TranslationFile) -> None:
            translation_file.content = translation_file.content.replace(
                "B:UseThisFileAsLanguageFile=false", "B:UseThisFileAsLanguageFile=true"
            )

        self.__paratranz_to_translation(
            filter_,
            after_to_translation_file_callback,
            ValueError("No gt lang file found"),
            "[自动化] 更新 GT 语言文件",
            repo_path,
            issue,
        )

    # endregion Gt Lang
