import os
import requests
from dotenv import load_dotenv
from utils import open_json_file

load_dotenv()
apikey = os.getenv("API_KEY")
print(apikey)


def get_exchange_rate(currency) -> float:
    """ Функция берет курс рубля с стороннего API"""

    base_url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": apikey}
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        return response.json()["rates"]["RUB"]
    return None


def convert_rub(transaction):
    """Функция конвертирует транзакции в валюте в рубли и возвращает сумму транзакции"""

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"].upper()

    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        rate = get_exchange_rate(currency)
        if rate:
            return float(amount) * rate


if __name__ == "__main__":
    transactions = open_json_file("../data/operations.json")
    for transaction in transactions:
        print(f"Сумма транцакции в рублях: {convert_rub(transaction)}")
