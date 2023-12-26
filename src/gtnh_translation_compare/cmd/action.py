import asyncio
import os
from pathlib import Path
from typing import TypeAlias, Callable, Optional

import httpx
from dulwich import porcelain

from gtnh_translation_compare import settings
from gtnh_translation_compare.filetypes import FiletypeLang, Language, FiletypeGTLang, Filetype
from gtnh_translation_compare.modpack.modpack import ModPack
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import Converter
from gtnh_translation_compare.paratranz.paratranz_cache import ParatranzCache
from gtnh_translation_compare.paratranz.types import TranslationFile
from gtnh_translation_compare.utils.file import ensure_lf

ParatranzFilenameFilter: TypeAlias = Callable[[str], bool]
AfterToTranslationFileCallback: TypeAlias = Callable[[TranslationFile], None]


class Action:
    def __init__(self) -> None:
        paratranz_project_id = settings.PARATRANZ_PROJECT_ID
        paratranz_token = settings.PARATRANZ_TOKEN

        self.client = ClientWrapper(
            client=httpx.AsyncClient(
                headers={"Authorization": paratranz_token},
                base_url="https://paratranz.cn/api",
                timeout=60,
            ),
            project_id=paratranz_project_id,
            cache_dir=settings.PARATRANZ_CACHE_DIR,
        )
        self.converter = Converter(
            client=self.client,
            cache=ParatranzCache(settings.PARATRANZ_CACHE_DIR),
            target_lang=settings.TARGET_LANG,
        )

    async def __paratranz_to_translation(
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
        all_files = await self.client.get_all_files()
        for f in all_files:
            if filter_(f.name):
                translation_file = await self.converter.to_translation_file(f)
                if after_to_translation_file_callback is not None:
                    after_to_translation_file_callback(translation_file)
                translation_files.append(translation_file)

        if len(translation_files) == 0:
            if raise_when_empty is not None:
                raise raise_when_empty

        if repo_path is None:
            for translation_file in translation_files:
                print("#" * 80)
                print(f"# {translation_file.relpath}")
                print("#" * 80)
                print(translation_file.content, end="\n\n")
            return

        for translation_file in translation_files:
            translation_filepath = os.path.abspath(os.path.join(repo_path, translation_file.relpath))
            translation_filepaths.append(translation_filepath)
            write_file(translation_filepath, translation_file.content)

        git_commit(
            repo_path,
            translation_filepaths,
            settings.GIT_AUTHOR,
            message,
            issue,
            settings.CLOSE_ISSUE_IN_COMMIT_MESSAGE,
        )

    ############################################################################
    # From Paratranz
    ############################################################################

    # Quest Book
    def paratranz_to_quest_book(
        self,
        repo_path: Optional[str] = None,
        issue: Optional[str] = None,
        commit_message: str = "[自动化] 更新 任务书",
    ) -> None:
        filter_: ParatranzFilenameFilter = lambda name: name == settings.DEFAULT_QUESTS_LANG_TARGET_REL_PATH + ".json"
        asyncio.run(
            self.__paratranz_to_translation(
                filter_,
                None,
                ValueError("No quest book file found"),
                commit_message,
                repo_path,
                issue,
            )
        )

    # Lang + Zs
    def paratranz_to_lang_and_zs(
        self,
        repo_path: Optional[str] = None,
        issue: Optional[str] = None,
        commit_message: str = "[自动化] 更新 语言文件 + 脚本",
    ) -> None:
        def filter_(name: str) -> bool:
            return any(
                [
                    name.endswith(".lang" + ".json")
                    and name != settings.DEFAULT_QUESTS_LANG_TARGET_REL_PATH + ".json"
                    and name != settings.GT_LANG_TARGET_REL_PATH + ".json",
                    name.endswith(".zs" + ".json"),
                ]
            )

        asyncio.run(
            self.__paratranz_to_translation(
                filter_,
                None,
                ValueError("No lang or zs file found"),
                commit_message,
                repo_path,
                issue,
            )
        )

    # Gt Lang
    def paratranz_to_gt_lang(
        self,
        repo_path: Optional[str] = None,
        issue: Optional[str] = None,
        commit_message: str = "[自动化] 更新 GT 语言文件",
    ) -> None:
        filter_: ParatranzFilenameFilter = lambda name: name == settings.GT_LANG_TARGET_REL_PATH + ".json"

        def after_to_translation_file_callback(translation_file: TranslationFile) -> None:
            translation_file.content = translation_file.content.replace(
                "B:UseThisFileAsLanguageFile=false", "B:UseThisFileAsLanguageFile=true"
            )

        asyncio.run(
            self.__paratranz_to_translation(
                filter_,
                after_to_translation_file_callback,
                ValueError("No gt lang file found"),
                commit_message,
                repo_path,
                issue,
            )
        )

    ############################################################################
    # To Paratranz
    ############################################################################

    # Quest Book
    async def _quest_book_to_paratranz(self, commit_sha: Optional[str] = None) -> None:
        if commit_sha is None or commit_sha == "":
            commit_sha = "master"
        qb_lang_file_url = (
            f"https://raw.githubusercontent.com"
            f"/{settings.GTNH_REPO}/{commit_sha}/{settings.DEFAULT_QUESTS_LANG_TEMPLATE_REL_PATH}"
        )
        res = httpx.get(url=qb_lang_file_url, timeout=60)
        if res.status_code != 200:
            raise ValueError(f"Failed to get quest book file from {qb_lang_file_url}")
        qb_lang_file = FiletypeLang(
            relpath=settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH, content=res.text, language=Language.en_US
        )
        qb_paratranz_file = await self.converter.to_paratranz_file(qb_lang_file)
        await self.client.upload_file(qb_paratranz_file)

    def quest_book_to_paratranz(self, commit_sha: Optional[str] = None) -> None:
        asyncio.run(self._quest_book_to_paratranz(commit_sha))

    # Lang + Zs
    async def _lang_and_zs_to_paratranz(self, modpack_path: str) -> None:
        modpack = ModPack(Path(modpack_path))
        # concurrency number
        sem = asyncio.Semaphore(10)

        async def upload_file(_sem: asyncio.Semaphore, lang_file: Filetype) -> None:
            async with _sem:
                paratranz_file = await self.converter.to_paratranz_file(lang_file)
                await self.client.upload_file(paratranz_file)

        tasks = [upload_file(sem, lang_file) for lang_file in modpack.lang_files]
        tasks += [upload_file(sem, script_file) for script_file in modpack.script_files]

        # noinspection PyTypeChecker
        await asyncio.gather(*tasks)

    def lang_and_zs_to_paratranz(self, modpack_path: str) -> None:
        asyncio.run(self._lang_and_zs_to_paratranz(modpack_path))

    # Gt Lang
    async def _gt_lang_to_paratranz(self, gt_lang_url: str) -> None:
        res = httpx.get(url=gt_lang_url, timeout=60)
        gt_lang_file = FiletypeGTLang(
            relpath=settings.GT_LANG_TARGET_REL_PATH,
            content=ensure_lf(res.text),
            language=Language.en_US,
        )
        gt_paratranz_file = await self.converter.to_paratranz_file(gt_lang_file)
        await self.client.upload_file(gt_paratranz_file)

    def gt_lang_to_paratranz(self, gt_lang_url: str) -> None:
        asyncio.run(self._gt_lang_to_paratranz(gt_lang_url))


def git_commit(
    git_root: str,
    paths: list[str],
    author: Optional[str],
    message: str,
    issue: Optional[str],
    close_issue_in_commit_message: bool,
) -> None:
    porcelain.add(git_root, paths)  # type: ignore[no-untyped-call]
    commit_message = message
    if issue is not None and close_issue_in_commit_message:
        commit_message += f"\n\nclosed #{issue}"
    porcelain.commit(  # type: ignore[no-untyped-call]
        git_root,
        message=commit_message,
        author=author,
    )


def write_file(filepath: str, content: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as fp:
        fp.write(content)
