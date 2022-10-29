from gtnh_translation_compare.utils.file import replace_illegal_characters, ensure_lf


def test_replace_illegal_characters() -> None:
    assert replace_illegal_characters("foo") == "foo"
    assert replace_illegal_characters("foo/bar") == "foo_bar"
    assert replace_illegal_characters("foo\\bar") == "foo_bar"
    assert replace_illegal_characters("foo:bar") == "foo_bar"
    assert replace_illegal_characters("foo<bar") == "foo_bar"
    assert replace_illegal_characters("foo>bar") == "foo_bar"
    assert replace_illegal_characters('foo"bar') == "foo_bar"
    assert replace_illegal_characters("foo|bar") == "foo_bar"
    assert replace_illegal_characters("foo?bar") == "foo_bar"
    assert replace_illegal_characters("foo*bar") == "foo_bar"


def test_ensure_lf() -> None:
    assert ensure_lf("foo") == "foo"
    assert ensure_lf("foo\r\nbar") == "foo\nbar"
    assert ensure_lf("foo\rbar") == "foo\nbar"
