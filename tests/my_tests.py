import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_number():
    return("1234567890123456")

@pytest.fixture
def wrong_length():
    return("12345678")

def test_correct_mask(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"

def test_length(wrong_length):
    assert get_mask_card_number(wrong_length) == wrong_length

def test_length_card_number(card_number):
    assert get_mask_card_number(card_number) ==