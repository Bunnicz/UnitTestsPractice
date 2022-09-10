from pay.order import LineItem


def test_line_item_default() -> None:
    line_item = LineItem("test", 150)
    assert line_item.total == 150


def test_line_item_custom() -> None:
    line_item = LineItem("test", 150, 2)
    assert line_item.total == 300
