"""
Docstring - простой и удобный способ добавить детальное описание в функцию.
(что-то вроде инструкции пользователя.

Извлечь можно с помощью функции help().
"""


def my_function():
    """
    This is my function: very simple and very useful and very good way to add a description.
    Return nothing.

    :return: None
    """
    print("Hello World")


print(help(my_function))
