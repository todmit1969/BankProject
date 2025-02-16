import pytest
from src.decorators import my_function


def test_my_function(capsys):
    with pytest.raises(TypeError):
        my_function(2, "3")
    captured = capsys.readouterr()
    assert "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (2, '3'), {}" in captured.out
