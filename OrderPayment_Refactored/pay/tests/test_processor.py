import os
from datetime import date

import pytest
from dotenv import load_dotenv
from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor, luhn_checksum

load_dotenv()

API_KEY = os.environ.get("API_KEY") or ""
CC_YEAR = date.today().year + 2


@pytest.fixture
def payment_processor() -> PaymentProcessor:
    return PaymentProcessor(API_KEY)


@pytest.fixture
def card() -> CreditCard:
    year = date.today().year + 2
    return CreditCard("1249190007575069", 12, year)


@pytest.fixture
def card_expired() -> CreditCard:
    year = date.today().year - 2
    return CreditCard("1249190007575069", 12, year)


@pytest.fixture
def card_wrong_number() -> CreditCard:
    year = date.today().year + 2
    return CreditCard("1249190007575068", 12, year)


#######TESTS########
def test_invalid_api_key(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        PaymentProcessor("").charge(card, 100)


def test_card_number_valid_date(
    payment_processor: PaymentProcessor, card: CreditCard
) -> None:
    assert payment_processor.validate_card(card)


def test_card_number_invalid_date(
    payment_processor: PaymentProcessor, card_expired: CreditCard
) -> None:
    assert not payment_processor.validate_card(card_expired)


def test_card_number_valid_luhn(card: CreditCard) -> None:
    assert luhn_checksum(card.number)


def test_card_number_invalid_luhn(card_wrong_number: CreditCard) -> None:
    assert not luhn_checksum(card_wrong_number.number)


def test_charge_card_valid(
    payment_processor: PaymentProcessor, card: CreditCard
) -> None:
    payment_processor.charge(card, 100)


def test_charge_card_invalid(
    payment_processor: PaymentProcessor, card_wrong_number: CreditCard
) -> None:
    with pytest.raises(ValueError):
        payment_processor.charge(card_wrong_number, 100)
