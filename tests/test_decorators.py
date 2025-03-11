import pytest

from src.decorators import my_function


def test_my_function(capsys):
    """ Функция проверяет работу функции декоратора"""
    with pytest.raises(TypeError):
        my_function(2, "3")
    captured = capsys.readouterr()
    assert "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (2, '3'), {}" in captured.out
