from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(bank_card_or_account: str) -> str:
    """Функция возвращает замаскированный номер карты или счета"""

    new_mask_account_card = ""
    card_account_name = ""
    card_account_number = ""
    for i in bank_card_or_account:
        if i.isalpha():
            card_account_name += i
        elif i.isdigit():
            card_account_number += i

    if len(card_account_number) > 16:
        new_mask_account_card = card_account_name + get_mask_card_number(card_account_number)
    elif len(card_account_number) == 16:
        new_mask_account_card = card_account_name + get_mask_card_number(card_account_number)

    return new_mask_account_card

print()