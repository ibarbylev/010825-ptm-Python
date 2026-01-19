"""assertEqual"""
import sys

import my_file
import unittest
from unittest.mock import patch


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


class TestSumKV(unittest.TestCase):
    """Создаем тестовый случай"""

    def test_equal(self):
        """Создаем сам тест"""

        # используем функцию assertEqual
        self.assertEqual(sum_of_squares(2, 3), 13)

    def test_not_equal(self):
        """используем функцию assertNotEqual"""
        self.assertNotEqual(sum_of_squares(2, 3), 10)

    def test_true(self):
        """используем функцию assertTrue"""
        self.assertTrue(val_compare(10, 3))

    def test_false(self):
        """используем функцию assertTrue"""
        self.assertFalse(val_compare(10, 30))

    def test_is(self):
        """используем функцию assertIs"""
        self.assertIs(A, B)

    def test_is_not(self):
        """используем функцию assertIsNot"""
        self.assertIsNot(Plane(), Plane())

    def test_is_none(self):
        """используем функцию assertIsNone"""
        self.assertIsNone(is_none(None))

    def test_is_not_none(self):
        """используем функцию assertIsNotNone"""
        self.assertIsNotNone(is_none("string"))

    def test_in(self):
        """используем функцию assertIn"""
        self.assertIn(1, [1, 2, 3])

    def test_not_in(self):
        """используем функцию assertNotIn"""
        self.assertNotIn(4, [1, 2, 3])

    def test_isinstance(self):
        """используем функцию assertIsInstance"""
        self.assertIsInstance(Plane(), Plane)

    def test_not_isinstance(self):
        """используем функцию assertNotIsInstance"""
        self.assertNotIsInstance(Plane(), Car)

    def test_raises_with_with(self):
        """используем функцию assertRaises"""
        with self.assertRaises(ZeroDivisionError):
            1 // 0

    def test_raises_without_with(self):
        """используем функцию assertRaises"""
        division_by_zero = lambda x: x / 0
        self.assertRaises(ZeroDivisionError, division_by_zero, 5)

# ======================================================================
# **********************************************************************
# ***                                                                ***
# *** More complex (and more interesting!) options for unit testing. ***
# ***                                                                ***
# **********************************************************************
# ======================================================================

    @patch.object(sys, 'argv', ['my_file.py', '-p'])   # sys.argv = ['my_file.py', '-p']
    def test_with_mock_patch_function_my_func_false_with_decorator(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        self.assertRaises(IndexError, my_file.parsing_command_line_parameters)

    def test_with_mock_patch_function_my_func_false_without_decorator(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        with patch.object(sys, 'argv', ['my_file.py', '-p']):
            self.assertRaises(IndexError, my_file.parsing_command_line_parameters)

    @patch.object(sys, 'argv', ['my_file.py', '-p', 7777])
    def test_with_mock_patch_function_my_func_true_with_decorator(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        self.assertEqual(7777, my_file.parsing_command_line_parameters())

    def test_with_mock_patch_function_my_func_true_without_decorator(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        with patch.object(sys, 'argv', ['my_file.py', '-p', 7777]):
            self.assertEqual(7777, my_file.parsing_command_line_parameters())


if __name__ == '__main__':
    unittest.main()
