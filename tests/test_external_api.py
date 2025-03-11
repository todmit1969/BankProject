from unittest.mock import Mock, patch

from src.external_api import convert_rub


@patch("requests.get")
def test_convert_rub(mock_get, convert_to_rub=7000):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates":{"RUB":70}}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {
                      "amount": "100",
                      "currency": {
                        "name": "USD",
                        "code": "USD"
                      }
                    }}

    result = convert_rub(transaction)

    assert convert_to_rub == result
    mock_get.assert_called_once()