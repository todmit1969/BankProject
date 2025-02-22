import json, os


def open_json_file(file_path):
    """Функция читает json файл и возвращает список словарейй с транзакциями"""

    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        return []
    with open(file_path, encoding="UTF-8") as json_file:
        transaction_list = json.load(json_file)
        if not isinstance(transaction_list, list) or len(transaction_list) == 0:
            return []
        else:
            return transaction_list

#print(open_json_file("../data/operations.json"))

