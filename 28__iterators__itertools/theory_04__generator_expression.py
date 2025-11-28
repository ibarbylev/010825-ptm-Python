"""
Генераторное выражение - частный случай итератора
"""

from typing import Iterable, Iterator, Generator

gen = (n for n in range(3))

print(gen)  # <generator object <genexpr> at 0x74bdc034da80>
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
try:
    print(next(gen))
except StopIteration as e:
    print(e.__class__.__name__, e.value)
    # StopIteration None


print(""" ===== Who is who? ===== """)

lst = [1, 2, 3, 4, 5]
lst_iter = iter(lst)
gen = (n for n in range(3))

print(isinstance(lst, Iterable))
print(isinstance(lst, Iterator))
print(isinstance(lst, Generator))
print()

print(isinstance(lst_iter, Iterable))
print(isinstance(lst_iter, Iterator))
print(isinstance(lst_iter, Generator))
print()

print(isinstance(gen, Iterable))
print(isinstance(gen, Iterator))
print(isinstance(gen, Generator))


"""
==============================================================================
Вопрос "на засыпку": Можно ли использовать генераторное выражение в цикле for?
==============================================================================
"""