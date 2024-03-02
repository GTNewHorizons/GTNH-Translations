from gtnh_translation_compare.utils.line_iterator import line_iterator


def test_line_iterator() -> None:
    content = "\n".join(["", "test", "", "测试", ""])
    result = list(line_iterator(content))
    assert result == [
        (0, "", 0, 0),
        (1, "test", 1, 5),
        (2, "", 6, 6),
        (3, "测试", 7, 9),
    ]
