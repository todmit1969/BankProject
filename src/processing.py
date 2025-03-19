from typing import Any, Dict
from mypy.strconv import indent


def filter_by_state(transactions_list: list[Dict[str, Any]], state: str) -> list[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    for item in transactions_list:
        # Фильтрация с проверкой наличия ключа
        filtered_list =list([item for item in transactions_list if 'state' in item and item['state'] == state])

    if not filtered_list:
        raise ValueError("Указанное значение статуса state отсутствует в списке словарей")

    return filtered_list


def sort_by_date(transactions_list: list[Dict[str, Any]],
                 sort_key: bool = True) -> list[Dict[str, Any]]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки и возвращает новый список,
     отсортированный по дате"""

    return sorted(transactions_list, key=lambda x: x["date"], reverse=sort_key)


#vocab_list = [
#    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#    {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"}
#]

#print(filter_by_state(vocab_list, "CANCELED"))
#print(sort_by_date(vocab_list))
