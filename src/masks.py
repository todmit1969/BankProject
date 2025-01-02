def get_mask_card_number(card_number: str) -> str:
    """Функция возвращающяя маску номера карты в формате 'XXXX XX** **** XXXX'"""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(bank_account: str) -> str:
    """Функция возвращающяя маску номера счета в формате '**XXXX'"""
    return f"**{bank_account[-4:]}"


if __name__ == "__main__":
    user_input = input("Введите номер карты: ")
    if not user_input.isdigit() or len(user_input) > 16:
        print("Введен не коректный номер карты! Номер должен содержать только 16 цифр!")
    else:
        print(get_mask_card_number(user_input))

    user_input = input("Введите номер банковского счета: ")
    if not user_input.isdigit():
        print("Введен не коректный номер счета! Номер должен содержать только цифры!")
    else:
        print(get_mask_account(user_input))
