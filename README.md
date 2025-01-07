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

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```
## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/READ.md).

## Лицензия:

Этот проект лицензирован по лицензии MIT.