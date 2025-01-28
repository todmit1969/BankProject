import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def correct_mask():
    return "Maestro 1596837868705199"

def test_correct_mask(correct_mask):
    assert mask_account_card(correct_mask) == "Maestro 1596 83** **** 5199"


@pytest.fixture
def not_corr_value():
    return "MasterCard 1247158300734726758"

def test_not_corr_value(not_corr_value):
    assert mask_account_card(not_corr_value) == "MasterCard Номер счета должен содержать 20 цифр!"

@pytest.fixture
def conv_date():
    return "2024-03-11T02:26:18.671407"

def test_date_conv(conv_date):
    assert get_date(conv_date) == "11.03.2024"