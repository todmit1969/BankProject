import pandas as pd
import json
from typing import Any, Dict, List


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция считывает транзакции из .csv файла и вовращает список словарей с транзакциями"""
    try:
        transactions_df = pd.read_csv(file_path, delimiter=";")
        transactions = transactions_df.to_dict(orient="records")
        return transactions
    #    return json.dumps(transactions, indent=4).encode("utf-8").decode("unicode_escape")
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except pd.errors.EmptyDataError:
        print("Файл пустой")
        return []


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция считывает транзакции из .xlsx файла и вовращает список словарей с транзакциями"""
    try:
        transactions_df = pd.read_excel(file_path)
        transactions = transactions_df.to_dict(orient="records")
        return transactions
        #return json.dumps(transactions, indent=4).encode("utf-8").decode("unicode_escape")
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except pd.errors.EmptyDataError:
        print("Файл пустой")
        return []


if __name__ == "__main__":

    file_path_csv = ("../data/transactions.csv").encode("utf-8").decode("unicode_escape")
    file_path_excel = ("../data/transactions_excel.xlsx").encode("utf-8").decode("unicode_escape")

    result_csv = read_csv_transactions(file_path_csv)
    result_excel = read_excel_transactions(file_path_excel)

    print(result_csv)
    print(result_excel)
