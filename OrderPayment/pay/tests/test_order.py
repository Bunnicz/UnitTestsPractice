from pay.order import LineItem, Order


def test_order_empty() -> None:
    order = Order()
    assert order.total == 0


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="test", price=150, quantity=2))
    assert order.total == 300
