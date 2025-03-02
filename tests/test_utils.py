from unittest.mock import patch, mock_open
from src.utils import open_json_file

@patch("builtins.open", new_callable=mock_open, read_data=None)
def test_open_json_file(mock_file, file_name=None):
    transaction_list = open_json_file("operations.json")
    assert transaction_list == []
