import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

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

@pytest.fixture
def currency_filter():
    return transactions

def test_filter_by_currency(currency_filter):
    tr_gn = filter_by_currency(currency_filter, "USD")
    assert next(tr_gn) == transactions[0]
    assert next(tr_gn) == transactions[1]

def test_transaction_descriptions(currency_filter):
    desc_gn = transaction_descriptions(currency_filter)
    assert next(desc_gn) == transactions[0]["description"]
    assert next(desc_gn) == transactions[1]["description"]