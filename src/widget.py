from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_card_or_account: str) -> str:
    """Функция возвращает замаскированный номер карты или счета"""

    new_mask_account_card = ""
    card_account_name = ""
    card_account_number = ""
    for i in bank_card_or_account:
        if i.isalpha() or i == " ":
            card_account_name += i
        elif i.isdigit():
            card_account_number += i

    if len(card_account_number) > 16:
        new_mask_account_card = f"{card_account_name}{get_mask_account(card_account_number)}"
    else:
        new_mask_account_card = f"{card_account_name}{get_mask_card_number(card_account_number)}"

    return new_mask_account_card


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_str: str) -> str:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""

    get_date_only = date_str.split("T")[0]
    year_, month_, day_ = get_date_only.split("-")

    return f"{day_}.{month_}.{year_}"


print(get_date("2024-03-11T02:26:18.671407"))
