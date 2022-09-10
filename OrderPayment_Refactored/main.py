import os

from dotenv import load_dotenv

from pay.credit_card import CreditCard
from pay.order import LineItem, Order
from pay.payment import pay_order
from pay.processor import PaymentProcessor


def read_card_info() -> CreditCard:
    """Get card credentials from user"""
    card = input("Please enter your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    return CreditCard(number=card, expiry_month=month, expiry_year=year)


def main():
    load_dotenv()
    api_key = os.environ.get("API_KEY") or ""
    payment_processor = PaymentProcessor(api_key)
    # Test card number: 1249190007575069

    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))

    # Read card info from user
    card = read_card_info()
    pay_order(order, card, payment_processor)


if __name__ == "__main__":
    main()
