"""
Изменение изменяемых типов данных внутри функции изменит их и снаружи.
Поэтому перед изменением нужно делать их копию.
Глубокую или поверхностную - зависит от типа данных.
"""


def func(lst: list) -> list:
    lst.append(4)
    return lst


lst = [1, 2, 3]

result = func(lst)
print(result)           # [1, 2, 3, 4]
print(lst)              # [1, 2, 3, 4]
print(result == lst)    # True


"""
Это плохой вариант.

===============================================================================

Поэтому функцию func придётся доработать:
"""

def modified_func(lst: list) -> list:
    new_lst = lst[:]
    new_lst.append(4)
    return new_lst


lst = [1, 2, 3]

result = modified_func(lst)
print(result)           # [1, 2, 3, 4]
print(lst)              # [1, 2, 3]
print(result == lst)    # False
