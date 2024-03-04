import asyncio
import datetime
import glob
import os
from pathlib import Path
import subprocess
from typing import TypeAlias, Callable, Optional

import httpx
from dulwich import porcelain
from loguru import logger

from gtnh_translation_compare import settings
from gtnh_translation_compare.filetypes import FiletypeLang, Language, FiletypeGTLang, Filetype
from gtnh_translation_compare.modpack.modpack import ModPack
from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.converter import Converter
from gtnh_translation_compare.paratranz.paratranz_cache import ParatranzCache
from gtnh_translation_compare.paratranz.types import TranslationFile
from gtnh_translation_compare.utils.file import ensure_lf

ParatranzFilenameFilter: TypeAlias = Callable[[str], bool]
ParatranzToLocalPathConverter: TypeAlias = Callable[[str], Path]
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
        repo_path: Path,
        subdirectory: Path,
        path_converter: Optional[ParatranzToLocalPathConverter] = None,
    ) -> list[str]:
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

        for translation_file in translation_files:
            base_path = repo_path / subdirectory
            translation_file_relpath = path_converter(translation_file.relpath) if path_converter is not None else translation_file.relpath
            translation_filepath = os.path.abspath(os.path.join(base_path, translation_file_relpath))
            translation_filepaths.append(translation_filepath)
            write_file(translation_filepath, translation_file.content)

        return translation_filepaths

    ############################################################################
    # From Paratranz
    ############################################################################

    async def _sync_from_paratranz(
        self,
        repo_path: Path,
        subdirectory: Path,
    ) -> None:
        files_to_commit: list[str] = []
        files_to_commit.extend(await self._paratranz_to_quest_book(repo_path, subdirectory))
        files_to_commit.extend(await self._paratranz_to_lang(repo_path, subdirectory))
        files_to_commit.extend(await self._paratranz_to_gt_lang(repo_path, subdirectory))

        git_commit(
            repo_path,
            files_to_commit,
            settings.GIT_AUTHOR,
            f"Sync {settings.TARGET_LANG.name} from ParaTranz",
        )

    def sync_from_paratranz(
        self,
        repo_path: str = ".",
        subdirectory: str = ".",
    ) -> None:
        asyncio.run(self._sync_from_paratranz(Path(repo_path), Path(subdirectory)))

    # Quest Book
    async def _paratranz_to_quest_book(
        self,
        repo_path: Path,
        subdirectory: Path,
    ) -> list[str]:
        filter_: ParatranzFilenameFilter = lambda name: name == settings.DEFAULT_QUESTS_LANG_TARGET_REL_PATH + ".json"
        return await self.__paratranz_to_translation(
                filter_,
                None,
                ValueError("No quest book file found"),
                repo_path,
                subdirectory,
                None,
        )

    # Lang
    async def _paratranz_to_lang(
        self,
        repo_path: Path,
        subdirectory: Path,
    ) -> list[str]:
        def filter_(name: str) -> bool:
            return any(
                [
                    name.endswith(".lang" + ".json")
                    and name != settings.DEFAULT_QUESTS_LANG_TARGET_REL_PATH + ".json"
                    and name != settings.GT_LANG_TARGET_REL_PATH + ".json",
                ]
            )
        # Existing projects use resource folder on PT
        path_converter_: ParatranzToLocalPathConverter = lambda path: Path('config/txloader/forceload') / os.path.relpath(path, Path('resources'))

        return await self.__paratranz_to_translation(
                filter_,
                None,
                ValueError("No lang file found"),
                repo_path,
                subdirectory,
                path_converter_,
        )

    # Gt Lang
    async def _paratranz_to_gt_lang(
        self,
        repo_path: Path,
        subdirectory: Path,
    ) -> list[str]:
        filter_: ParatranzFilenameFilter = lambda name: name == settings.GT_LANG_TARGET_REL_PATH + ".json"

        def after_to_translation_file_callback(translation_file: TranslationFile) -> None:
            translation_file.content = translation_file.content.replace(
                "B:UseThisFileAsLanguageFile=false", "B:UseThisFileAsLanguageFile=true"
            )
        path_converter_: ParatranzToLocalPathConverter = lambda path: Path(f"GregTech_{settings.TARGET_LANG.name}.lang")

        return await self.__paratranz_to_translation(
                filter_,
                after_to_translation_file_callback,
                ValueError("No gt lang file found"),
                repo_path,
                subdirectory,
                path_converter_,
        )

    ############################################################################
    # To Paratranz
    ############################################################################

    # Gt Lang
    async def _gt_lang_to_paratranz(
        self,
        repo_path: Path,
        subdirectory: Path,
    ) -> None:
        base_path: Path = repo_path / subdirectory
        with open(base_path / settings.GT_LANG_TARGET_REL_PATH, 'r', encoding='UTF-8') as f:
            gt_lang_file = FiletypeGTLang(
                relpath=settings.GT_LANG_TARGET_REL_PATH,
                content=ensure_lf(f.read()),
                language=Language.en_US,
            )
        gt_paratranz_file = await self.converter.to_paratranz_file(gt_lang_file)
        await self.client.upload_file(gt_paratranz_file)

    def gt_lang_to_paratranz(
        self,
        repo_path: str = ".",
        subdirectory: str = "."
    ) -> None:
        asyncio.run(self._gt_lang_to_paratranz(Path(repo_path), Path(subdirectory)))

    # Commit changes made to nightly modpack
    async def _save_nightly_modpack_history(
            self,
            modpack_path: Path,
            repo_path: Path,
            subdirectory: Path,
    ) -> None:
        def get_relpath(path):
            return repo_path / subdirectory / path

        paths_to_commit: list[str] = []
        modpack = ModPack(Path(modpack_path))
        for lang_file in modpack.lang_files:
            relpath = get_relpath(lang_file.get_en_us_relpath())
            write_file(os.path.abspath(relpath), lang_file.content)
            paths_to_commit.append(relpath)

        qb_lang_file_url = (
            f"https://raw.githubusercontent.com"
            f"/{settings.GTNH_REPO}/master/{settings.DEFAULT_QUESTS_LANG_TEMPLATE_REL_PATH}"
        )
        res = httpx.get(url=qb_lang_file_url, timeout=60)
        if res.status_code != 200:
            raise ValueError(f"Failed to get quest book file from {qb_lang_file_url}")
        relpath = get_relpath(settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH)
        write_file(os.path.abspath(relpath), res.text)
        paths_to_commit.append(relpath)

        git_commit(
            repo_path,
            paths_to_commit,
            settings.GIT_AUTHOR,
            f"Nightly modpack {str(datetime.date.today())}",
        )

    def save_nightly_modpack_history(
            self,
            modpack_path: str,
            repo_path: str = ".",
            subdirectory: str = ".",
    ) -> None:
        asyncio.run(self._save_nightly_modpack_history(Path(modpack_path), Path(repo_path), Path(subdirectory)))

    # Sync files that have actually been changed compared to last nightly modpack to ParaTranz, excluding GregTech.lang
    async def _conditional_sync_to_paratranz(
            self,
            repo_path: Path,
            subdirectory: Path,
    ) -> None:
        base_path: Path = repo_path / subdirectory
        with subprocess.Popen(['git', 'diff', '--name-only', 'HEAD^..HEAD'], encoding='UTF-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
            changed_relpaths: list[str] = [os.path.relpath(str.strip(line), base_path) for line in p.stdout]
            logger.info('detected lang updates:')
            for change in changed_relpaths:
                logger.info(change)
            logger.info('#'*30)

        if settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH in changed_relpaths:
            with open(base_path / settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH, 'r', encoding='UTF-8') as f:
                content = f.read()
            qb_lang_file = FiletypeLang(
                relpath=settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH, content=content, language=Language.en_US
            )
            qb_paratranz_file = await self.converter.to_paratranz_file(qb_lang_file)
            await self.client.upload_file(qb_paratranz_file)
            changed_relpaths.remove(settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH)

        lang_files = []
        for file_path in changed_relpaths:
            if 'resources' not in file_path:
                logger.warning(f'Suspecious file detected in changed files: {file_path}')
                continue
            with open(base_path / file_path, 'r', encoding='UTF-8') as f:
                content = f.read()
            lang_files.append(FiletypeLang(file_path, content))

        # concurrency number
        sem = asyncio.Semaphore(10)

        async def upload_file(_sem: asyncio.Semaphore, lang_file: Filetype) -> None:
            async with _sem:
                paratranz_file = await self.converter.to_paratranz_file(lang_file)
                await self.client.upload_file(paratranz_file)

        tasks = [upload_file(sem, lang_file) for lang_file in lang_files]

        # noinspection PyTypeChecker
        await asyncio.gather(*tasks)

    def conditional_sync_to_paratranz(
            self,
            repo_path: str = ".",
            subdirectory: str = ".",
    ) -> None:
        asyncio.run(self._conditional_sync_to_paratranz(Path(repo_path), Path(subdirectory)))

    # Sync all the files to ParaTranz. GregTech.lang is handled by the caller.
    async def _sync_all_to_paratranz(
            self,
            repo_path: Path,
            subdirectory: Path,
    ) -> None:
        base_path: Path = repo_path / subdirectory
        with open(base_path / settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH, 'r', encoding='UTF-8') as f:
            content = f.read()
        qb_lang_file = FiletypeLang(
            relpath=settings.DEFAULT_QUESTS_LANG_EN_US_REL_PATH, content=content, language=Language.en_US
        )
        qb_paratranz_file = await self.converter.to_paratranz_file(qb_lang_file)
        await self.client.upload_file(qb_paratranz_file)

        lang_files = []
        for file_path in glob.glob(f'./{base_path}/resources/*/lang/en_US.lang'):
            with open(file_path, 'r', encoding='UTF-8') as f:
                content = f.read()
            lang_files.append(FiletypeLang(os.path.relpath(file_path, base_path), content))

        # concurrency number
        sem = asyncio.Semaphore(10)

        async def upload_file(_sem: asyncio.Semaphore, lang_file: Filetype) -> None:
            async with _sem:
                paratranz_file = await self.converter.to_paratranz_file(lang_file)
                await self.client.upload_file(paratranz_file)

        tasks = [upload_file(sem, lang_file) for lang_file in lang_files]

        # noinspection PyTypeChecker
        await asyncio.gather(*tasks)

        await self._gt_lang_to_paratranz(repo_path, subdirectory)

    def sync_all_to_paratranz(
            self,
            repo_path: str = ".",
            subdirectory: str = ".",
    ) -> None:
        asyncio.run(self._sync_all_to_paratranz(Path(repo_path), Path(subdirectory)))


def git_commit(
    git_root: str,
    paths: list[str],
    author: Optional[str],
    message: str,
) -> None:
    porcelain.add(git_root, paths)  # type: ignore[no-untyped-call]
    porcelain.commit(  # type: ignore[no-untyped-call]
        git_root,
        message=message,
        author=author,
        committer=author,
    )


def write_file(filepath: str, content: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as fp:
        fp.write(content)
