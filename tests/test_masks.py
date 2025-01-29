import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_number():
    return("1234567890123456")

def test_correct_mask(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"


@pytest.fixture
def wrong_length():
    return("12345678")

def test_length(wrong_length):
    assert get_mask_card_number(wrong_length) == "Неправильно указан номер карты!"


@pytest.fixture
def wrong_number():
    return("132ewsf994784ewf")

def test_wrong_number(wrong_number):
    assert get_mask_card_number(wrong_number) == "Номер не может содержать буквы!"


@pytest.fixture
def acc_number():
    return "12345678901234567890"

def test_account_mask(acc_number):
    assert get_mask_account(acc_number) == "**7890"


@pytest.fixture
def wrong_acc_length():
    return "12345678"

def test_length_acc_number(wrong_acc_length):
    assert get_mask_account(wrong_acc_length) == "Номер счета должен содержать 20 цифр!"


@pytest.fixture
def not_digit_acc_number():
    return "122454relksdlpwr000924"

def test_digits_acc_number(not_digit_acc_number):
    assert get_mask_account(not_digit_acc_number) == "Номер счета должен содержать только цифры!"
