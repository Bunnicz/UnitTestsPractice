from pay.processor import PaymentProcessor
from datetime import datetime
import pytest


API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

# charge ValueError
def test_api_key_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2024, 100)


def test_card_invalid_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575069", 12, 1999, 100)


def test_card_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2024, 100)


def test_card_number_valid_luhn() -> None:
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum("1249190007575069") == True


def test_card_number_invalid_luhn() -> None:
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum("1249190007575068") == False


def test_charge_card_valid() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2024, 100)


def test_charge_card_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575068", 12, 2024, 100)
