# Проект BankProject

## Описание:

Проект BankProject - это банковское приложение, которое разширяет пользовательские функции.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/todmit1969/BankProject.git
```
2. Перейдите в директорию проекта.
```
cd BankProject
```
3. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
```
python
from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card
from src.generators import filter_by_currency, transaction_descriptions,
                            card_number_generator

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)

# Пример использования get_mask_card_number
card_number = get_mask_card_number(1234567890123456)

# Пример использования get_mask_account
acc_number = get_mask_account(12345678901234567890)

# Пример использования mask_account_card
mask = mask_account_card("Maestro 1596837868705199")
mask = mask_account_card("Счет 64686473678894779589")

# Пример использования filter_by_currency
transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07","currency":
                                {"name": "USD","code": "USD"}
                                },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93","currency":
                                {"name": "USD","code": "USD"}
                                },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

# Пример использования transaction_descriptions
tran_desc = transaction_descriptions(transactions)
for _ in range(2):
    print(next(tran_desc))
    
# Пример использования card_number_generator
for card_number in card_number_generator(1, 4):
    print(card_number)
```

## Тестирование
Тесты находятся в папке tests. Для каждого тестируемого модуля
имя файла test_<имя модуля>.py.

В модуле masks тестируются функции get_mask_card_number 
и get_mask_account.
Тестируются:
- правильность маскирования;
- проверка работы функций с различными длинами и форматами 
    номеров счетов и карт
- проверка, что функции правильно отрабатывают входные строки
    где нет номера карты или счета, или длина меньше/больше ожидаемой.

В модуле widget тестируются функции mask_account_card и
get_data.
Для функции mask_account_card:
- Тесты для проверки, что функция корректно распознает и применяет нужный 
тип маскировки в зависимости от типа входных данных (карта или счет).
  - Параметризованные тесты с разными типами карт и счетов
для проверки универсальности функции.
- Тестирование функции на обработку некорректных 
входных данных и проверка ее устойчивости к ошибкам.
Для функции get_data:
- Тестирование правильности преобразования даты.
- Проверка работы функции на различных входных форматах
даты, включая граничные случаи и нестандартные строки
с датами.
- Проверка, что функция корректно обрабатывает входные 
строки, где отсутствует дата.

В модуле processing тестируются функции filter_by_state и
sort_by_date.
Для функции filter_by_state:
- Тестирование фильтрации списка словарей по заданному
статусу state.
- Проверка работы функции при отсутствии словарей с 
указанным статусом state в списке.
- Параметризация тестов для различных возможных значений
статуса state
Для функции sort_by_date:
- Тестирование сортировки списка словарей по датам в 
порядке убывания и возрастания.
- Проверка корректности сортировки при одинаковых датах.
- Тесты на работу функции с некорректными или нестандартными
форматами дат.

В модуле generators тестируются функции filter_by_currency, transaction_descriptions
и card_number_generator
Для функции filter_by_currency:
- Проверка что функция корректно фильтрует транзакции по заданной валюте.
- Проверка, что функция правильно обрабатывает случаи, когда транзакции
в заданной валюте отсутствуют.
Для функции transaction_descriptions:
- Проверка, что функция возвращает корректные описания для 
каждой транзакции.
- Тестируется работа функции с различным количеством входных транзакций,
включая пустой список.
Для функции card_number_generator:
- Проверка, что генератор выдает правильные номера карт в заданном диапазоне.
- Проверка корректности форматирования номеров карт.
- Проверка, что генератор корректно обрабатывает крайние значения
диапазона и правильно завершает генерацию.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/READ.md).

## Лицензия:

Этот проект лицензирован по лицензии MIT.