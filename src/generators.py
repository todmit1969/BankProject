transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]


def filter_by_currency(transactions, currency_code):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] != currency_code:
            continue
        else:
            yield transaction

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions):
    for transaction in transactions:
        description = transaction["description"]
        yield description

tran_desc = transaction_descriptions(transactions)
for _ in range(2):
    print(next(tran_desc))

def card_number_generator(start, stop):
    for num in range(start, stop):
        num = f"0000 0000 0000 000{num}"
        yield(num)

for card_number in card_number_generator(1, 6):
    print(card_number)
