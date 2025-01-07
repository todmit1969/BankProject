import typing


def filter_by_state(
    transactions_list: list[typing.Dict[typing.Any, str]], state: str
) -> list[typing.Dict[typing.Any, str]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    list_executed = []
    list_canceled = []
    for transaction in transactions_list:
        if transaction["state"] == "EXECUTED":
            list_executed.append(transaction)
        else:
            list_canceled.append(transaction)

    if state == "EXECUTED":
        return list_executed
    else:
        return list_canceled


def sort_by_date(transactions_list: list[dict[typing.Any, str]], sort_key: bool = True) -> list[dict[typing.Any, str]]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки и возвращает новый список,
     отсортированный по дате"""

    return sorted(transactions_list, key=lambda x: x["date"], reverse=sort_key)


vocab_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(vocab_list, "EXECUTED"))
print(sort_by_date(vocab_list))
