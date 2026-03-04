from gtnh_translation_compare.paratranz.client_wrapper import ClientWrapper
from gtnh_translation_compare.paratranz.types import FileExtra, ParatranzFile, Property, StringItem


def _new_paratranz_file(*items: StringItem) -> ParatranzFile:
    return ParatranzFile(
        file_name="resources/example/lang/en_US.lang.json",
        file_extra=FileExtra(
            original="",
            properties={"a": Property(key="a", start=0, end=0)},
            en_us_relpath="resources/example/lang/en_US.lang",
            target_relpath="resources/example/lang/ru_RU.lang",
        ),
        string_items=list(items),
    )


def test_prepare_sync_plan_updates_only_changed_rows() -> None:
    old_strings = [
        StringItem(id=1, key="a", original="old-a", translation="ta", stage=1),
        StringItem(id=2, key="b", original="old-b", translation="", stage=None),
    ]
    paratranz_file = _new_paratranz_file(
        StringItem(key="a", original="old-a", translation=""),
        StringItem(key="b", original="new-b", translation=""),
    )

    sync_plan = ClientWrapper._prepare_string_sync_plan(old_strings, paratranz_file)

    assert sync_plan.removed_ids == []
    assert sync_plan.added_strings == []
    assert len(sync_plan.updated_strings) == 1
    assert sync_plan.updated_strings[0].key == "b"
    assert sync_plan.updated_strings[0].id == 2


def test_prepare_sync_plan_marks_added_key() -> None:
    old_strings = [StringItem(id=1, key="a", original="old-a", translation="ta", stage=1)]
    paratranz_file = _new_paratranz_file(
        StringItem(key="a", original="old-a", translation=""),
        StringItem(key="b", original="new-b", translation=""),
    )

    sync_plan = ClientWrapper._prepare_string_sync_plan(old_strings, paratranz_file)

    assert sync_plan.removed_ids == []
    assert len(sync_plan.added_strings) == 1
    assert sync_plan.added_strings[0].key == "b"
    assert sync_plan.updated_strings == []


def test_prepare_sync_plan_marks_removed_key() -> None:
    old_strings = [
        StringItem(id=1, key="a", original="old-a", translation="ta", stage=1),
        StringItem(id=2, key="b", original="old-b", translation="", stage=None),
    ]
    paratranz_file = _new_paratranz_file(
        StringItem(key="a", original="old-a", translation=""),
    )

    sync_plan = ClientWrapper._prepare_string_sync_plan(old_strings, paratranz_file)

    assert sync_plan.removed_ids == [2]
    assert sync_plan.added_strings == []
    assert sync_plan.updated_strings == []
