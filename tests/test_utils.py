from unittest.mock import patch, mock_open
from src.utils import open_json_file

@patch("builtins.open", new_callable=mock_open, read_data='{"id": "441945886"}')
def test_open_json_file(mock_file, transaction_list):
    transactions = open_json_file("..\tests\test.json")
    assert transactions == {"test"}