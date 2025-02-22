import requests, json, os
from utils import open_json_file
from dotenv import load_dotenv


load_dotenv()
apikey = os.getenv("API_KEY")
print(apikey)

def get_exchange_rate(currency) -> float:
    base_url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": apikey}
    print(headers)
    response = requests.get(base_url, headers=headers)
    print(response.text)
    if response.status_code == 200:
        return response.json()["rates"]["RUB"]
    return None


def convert_rub(transaction):
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"].upper()

    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        rate = get_exchange_rate(currency)
        print(rate)
        if rate:
            return float(amount) * rate
    #return 0.0


if __name__ == "__main__":
    transactions = open_json_file("../data/operations.json")
    for transaction in transactions:
        print(f"Сумма транцакции в рублях: {convert_rub(transaction)}")
