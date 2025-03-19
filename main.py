from src.utils import open_json_file
from src.read_transactions import read_excel_transactions, read_csv_transactions
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.filtered_transactions import get_trans_by_desc
from src.count_transactions import count_transactions_by_category
from src.categories import get_categories
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data")
currency_key = 0

def main() -> None:
    """Фунция отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print('''Выберите необходимый пункт меню: 
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла
            ''')
    answer_1 = input("Введите Ваш выбор: ")
    if answer_1 == "1":
        print("Для обработки выбран JSON-файл.")
        file_path = os.path.join(DATA_PATH, "operations.json").encode("utf-8")
        file_choosen = open_json_file(file_path)
        currency_key = 1
    elif answer_1 == "2":
        print("Для обработки выбран CSV-файл.")
        file_path = os.path.join(DATA_PATH, "transactions.csv")
        file_choosen = read_csv_transactions(file_path)
        currency_key = 2
    else:
        print("Для обработки выбран XLSX-файл.")
        file_path = os.path.join(DATA_PATH, "transactions_excel.xlsx")
        file_choosen = read_excel_transactions(file_path)
        print(file_choosen)
        currency_key = 3

    print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    while True:
        answer_2 = input("Введите Ваш выбор: ").upper()
        if answer_2 == "EXECUTED" or answer_2 == "CANCELED" or answer_2 == "PENDING":
            filtered_trans = filter_by_state(file_choosen, answer_2)
            break
        elif answer_2 == "":
            print(f"Статус операции {answer_2} недоступен.")
        else:
            print(f"Статус операции {answer_2} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")

    while True:
        answer_3 = input("Введите Ваш выбор: ").lower()
        if answer_3 == "да" or answer_3 == "нет":
            break
        if answer_3 != "да" or answer_3 !="нет" or answer_3 == "":
            print("Введите да или нет!")

    if answer_3 == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        answer_4 = input("Введите Ваш выбор: ").lower()
        if answer_4 == "по возрастанию":
            sort_key = True
        else:
            sort_key = False
    else:
        sort_key = False
    trans_date_sorted = sort_by_date(filtered_trans, sort_key)

    print("Выводить только рублевые тразакции? Да/Нет")
    while True:
        answer_5 = input("Введите Ваш выбор: ").lower()
        if answer_5 == "да":
            currency_code = "RUB"
            break
        elif answer_5 == "нет":
            currency_code = " "
            break
        else:
            print("Введите Да или Нет!")

    filtered_by_cur_trans = filter_by_currency(trans_date_sorted, currency_code, currency_key)

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer_6 = input("Введите Ваш выбор: ").lower()
    if answer_6 == "да":
        word_to_search = input("Введите слово: ")
        trans_by_desc = get_trans_by_desc(filtered_by_cur_trans, word_to_search)
        print("Распечатываю итоговый список транзакций...")
        categories = get_categories(trans_by_desc)
        result = count_transactions_by_category(trans_by_desc, categories)
        print(result)
    else:
        print("Распечатываю итоговый список транзакций...")
        categories = get_categories(filtered_by_cur_trans)
        result = count_transactions_by_category(filtered_by_cur_trans, categories)
        print(result)




if __name__ == "__main__":
    main()