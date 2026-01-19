import sys
from unittest.mock import patch
import pytest  # только для pytest.raises
import my_file


def sum_of_squares(i, j):
    """Сумма квадратов"""
    return i ** 2 + j ** 2


def val_compare(val_1, val_2):
    """Сравнение значений"""
    return val_1 > val_2


class Plane:
    """class"""
    pass


class Car:
    """class"""
    pass


def is_compare(val_1, val_2):
    return val_1 is val_2


def is_none(val_1):
    val_2 = val_1
    return val_2


A = 5
B = A


class TestMathFunctions:
    def test_equal(self):
        assert sum_of_squares(2, 3) == 13

    def test_not_equal(self):
        assert sum_of_squares(2, 3) != 10

    def test_true(self):
        assert val_compare(10, 3) is True

    def test_false(self):
        assert val_compare(10, 30) is False

    def test_is(self):
        assert A is B

    def test_is_not(self):
        assert Plane() is not Plane()

    def test_is_none(self):
        assert is_none(None) is None

    def test_is_not_none(self):
        assert is_none("string") is not None

    def test_in(self):
        assert 1 in [1, 2, 3]

    def test_not_in(self):
        assert 4 not in [1, 2, 3]

    def test_isinstance(self):
        assert isinstance(Plane(), Plane)

    def test_not_isinstance(self):
        assert not isinstance(Plane(), Car)


class TestExceptions:
    def test_raises_with_context_manager(self):
        with pytest.raises(ZeroDivisionError):
            1 // 0


class TestMocking:
    def test_with_mock_patch_function_my_func_false(self):
        with patch.object(sys, 'argv', ['my_file.py', '-p']):
            with pytest.raises(IndexError):
                my_file.parsing_command_line_parameters()

    def test_with_mock_patch_function_my_func_true(self):
        with patch.object(sys, 'argv', ['my_file.py', '-p', 7777]):
            assert my_file.parsing_command_line_parameters() == 7777