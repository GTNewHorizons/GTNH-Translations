from gtnh_translation_compare.utils.unicode import to_unicode


def test_to_unicode() -> None:
    assert to_unicode("foo") == "\\u0066\\u006f\\u006f"
    assert to_unicode("foo bar") == "\\u0066\\u006f\\u006f\\u0020\\u0062\\u0061\\u0072"
    assert to_unicode("foo bar baz") == "\\u0066\\u006f\\u006f\\u0020\\u0062\\u0061\\u0072\\u0020\\u0062\\u0061\\u007a"
    assert to_unicode("张三") == "\\u5f20\\u4e09"
    assert to_unicode("张三 李四") == "\\u5f20\\u4e09\\u0020\\u674e\\u56db"
    assert to_unicode("张三 李四 王五") == "\\u5f20\\u4e09\\u0020\\u674e\\u56db\\u0020\\u738b\\u4e94"
    assert to_unicode("foo\nbar") == "\\u0066\\u006f\\u006f\\u000a\\u0062\\u0061\\u0072"
    assert (
        to_unicode("hello world, 你好世界") == "\\u0068\\u0065\\u006c\\u006c\\u006f"
        "\\u0020"
        "\\u0077\\u006f\\u0072\\u006c\\u0064\\"
        "u002c\\u0020"
        "\\u4f60\\u597d\\u4e16\\u754c"
    )
