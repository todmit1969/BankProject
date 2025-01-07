def filter_by_state(vocab_list: list[dict], state: str= "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    list_executed = []
    list_canceled = []
    for i in vocab_list:
        if i["state"] == "EXECUTED":
            list_executed.append(i)
        else:
            list_canceled.append(i)

    return list_executed

def sort_by_date(vocab_list: list[dict], sort_key=True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки и возвращает новый список,
     отсортированный по дате"""

    return sorted(vocab_list, key=lambda x: x["date"],reverse=sort_key)

vocab_list = ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                       {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                       {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                       {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}])

print(filter_by_state(vocab_list))
print(sort_by_date(vocab_list))