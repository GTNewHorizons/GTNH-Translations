from gtnh_translation_compare.filetypes.filetype_script import FiletypeScript
from gtnh_translation_compare.filetypes.property import Property
import pytest

RELPATH = "test/x/test.zs"
CONTENT = "\n".join(
    [
        "// test",
        'game.setLocalization("en_US", "test", "test");',
        'game.setLocalization("test2", "test2");',
        'NEI.overrideName(<Test:test:3>, "test3");',
        'NEI.overrideName(Test4, "test4");',
        '<Test:test5>.addTooltip("test5");',
        '<Test:test6>.withTag({type: "test"}).addTooltip("test6");',
        "",
        '<Test:test7>.addShiftTooltip("test7.1");',
        '<Test:test7>.addShiftTooltip("test7.2");',
        '<Test:test7>.addShiftTooltip("test7.3");',
        "",
        '<Test:test8>.displayName = "test8";',
    ]
)


@pytest.fixture(scope="module")
def filetype_script() -> FiletypeScript:
    return FiletypeScript(RELPATH, CONTENT)


def test__get_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.relpath == RELPATH


def test__get_content(filetype_script: FiletypeScript) -> None:
    assert filetype_script.content == CONTENT


def test__get_properties(filetype_script: FiletypeScript) -> None:
    assert filetype_script.properties == {
        'script+test.zs+game.setLocalization+"test"': Property(
            'script+test.zs+game.setLocalization+"test"', 'game.setLocalization("en_US", "test", "test");', 8, 54
        ),
        'script+test.zs+game.setLocalization+"test2"': Property(
            'script+test.zs+game.setLocalization+"test2"', 'game.setLocalization("test2", "test2");', 55, 94
        ),
        "script+test.zs+NEI.overrideName+<Test:test:3>": Property(
            "script+test.zs+NEI.overrideName+<Test:test:3>", 'NEI.overrideName(<Test:test:3>, "test3");', 95, 136
        ),
        "script+test.zs+NEI.overrideName+Test4": Property(
            "script+test.zs+NEI.overrideName+Test4", 'NEI.overrideName(Test4, "test4");', 137, 170
        ),
        "script+test.zs+addTooltip+<Test:test5>": Property(
            "script+test.zs+addTooltip+<Test:test5>", '<Test:test5>.addTooltip("test5");', 171, 204
        ),
        'script+test.zs+addTooltip+<Test:test6>.withTag({type: "test"})': Property(
            'script+test.zs+addTooltip+<Test:test6>.withTag({type: "test"})',
            '<Test:test6>.withTag({type: "test"}).addTooltip("test6");',
            205,
            262,
        ),
        "script+test.zs+addShiftTooltip+<Test:test7>": Property(
            "script+test.zs+addShiftTooltip+<Test:test7>",
            "\n".join(
                [
                    '<Test:test7>.addShiftTooltip("test7.1");',
                    '<Test:test7>.addShiftTooltip("test7.2");',
                    '<Test:test7>.addShiftTooltip("test7.3");',
                ]
            ),
            264,
            386,
        ),
        "script+test.zs+displayName+<Test:test8>": Property(
            "script+test.zs+displayName+<Test:test8>", '<Test:test8>.displayName = "test8";', 388, 423
        ),
    }


def test_get_en_us_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.get_en_us_relpath() == RELPATH


def test_get_zh_cn_relpath(filetype_script: FiletypeScript) -> None:
    assert filetype_script.get_zh_cn_relpath() == RELPATH
