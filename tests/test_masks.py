import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('number, expected', [
        ('1234567890123456', '1234 56** **** 3456'),
        ("654", "Неправильно указан номер карты!"),
        ("abcd4567efgh3456", "Номер не может содержать буквы!")
])
def test_correct_mask(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize('ac_number, expected', [
        ('12345678901234567890', '**7890'),
        ("654", "Номер счета должен содержать 20 цифр!"),
        ("abcd4567efgh3456rtyj", "Номер счета должен содержать только цифры!")
])

def test_correct_acc_mask(ac_number, expected):
    assert get_mask_account(ac_number) == expected
