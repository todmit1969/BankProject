import logging


logger = logging.getLogger("masks.log")
file_handler = logging.FileHandler("C:\\Users\\tmitev\\PycharmProjects\\BankProject\\logs\\masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция возвращающяя маску номера карты в формате 'XXXX XX** **** XXXX'"""
    logger.info(f"Запускается функция get_mask_card_number с входными данными {card_number}...")
    if len(card_number) != 16:
        logger.error("Неверные данные")
        return "Неправильно указан номер карты!"
    elif not card_number.isdigit():
        logger.error("Неверные данные")
        return "Номер не может содержать буквы!"
    elif len(card_number) == 16:
        logger.info("Номер карты успешно преобразован")
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return None


def get_mask_account(bank_account: str) -> str:
    """Функция возвращающяя маску номера счета в формате '**XXXX'"""
    logger.info(f"Запускается функция get_mask_account с входными данными {bank_account}...")
    if len(bank_account) != 20 and bank_account.isdigit():
        logger.error("Неверные данные")
        return("Номер счета должен содержать 20 цифр!")
    elif not bank_account.isdigit():
        logger.error("Неверные данные")
        return ("Номер счета должен содержать только цифры!")
    elif len(bank_account) == 20 and bank_account.isdigit():
        logger.info("Номер счета успешно преобразован")
        return f"**{bank_account[-4:]}"
    else:
        return None


if __name__ == "__main__":
    user_input = input("Введите номер карты: ")
    if not user_input.isdigit() or len(user_input) > 16 or len(user_input) < 16:
        logger.error("Неверные данные")
        print("Введен не коректный номер карты! Номер должен содержать только 16 цифр!")
    else:
        logger.info("Номер карты успешно преобразован")
        print(get_mask_card_number(user_input))

    user_input = input("Введите номер банковского счета: ")
    if not user_input.isdigit():
        logger.error("Неверные данные")
        print("Введен не коректный номер счета! Номер должен содержать только цифры!")
    else:
        logger.info("Номер счета успешно преобразован")
        print(get_mask_account(user_input))
