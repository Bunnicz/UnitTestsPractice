from datetime import date

import pytest
from pay.credit_card import CreditCard
from pay.order import LineItem, Order, OrderStatus
from pay.payment import pay_order


# possible to use fixture instead and return PaymentProcessorMock
class PaymentProcessorMock:
    def charge(self, card: CreditCard, amount: int) -> None:
        print(f"Charging card number {card} for ${amount/100:.2f}")


@pytest.fixture
def payment_processor_mock() -> PaymentProcessorMock:
    return PaymentProcessorMock()


@pytest.fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard("1249190007575069", 12, year)


#######TESTS########
def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem(name="test", price=100))
    pay_order(order, card, PaymentProcessorMock())
    assert order.status == OrderStatus.PAID


def test_pay_order_invalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        order = Order()
        pay_order(order, card, PaymentProcessorMock())
