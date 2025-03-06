import json
import logging
import os

logger = logging.getLogger("utils.log")
file_handler = logging.FileHandler("C:\\Users\\tmitev\\PycharmProjects\\BankProject\\logs\\utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def open_json_file(file_path):
    """Функция читает json файл и возвращает список словарейй с транзакциями"""
    logger.info(f"Запускается функция open_json_file с входными данными {file_path}...")
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        logger.error("Неверные данные")
        return []
    try:
        with open(file_path, encoding="UTF-8") as json_file:
            transaction_list = json.load(json_file)
            if not isinstance(transaction_list, list) or len(transaction_list) == 0:
                logger.error("Неверные данные")
                return []
            else:
                logger.info("Функция успешно завершена!")
                return transaction_list
    except (json.JSONDecodeError, FileNotFoundError) as er:
        logger.error("Неверные данные: ошибка {er}")
        return []


if __name__ == "__main__":
    tt = open_json_file("C:\\Users\\tmitev\\PycharmProjects\\BankProject\\data\\operation.json")
    print(tt)