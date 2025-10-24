"""Методы (и способы) создания множества"""


print(""" 1. =============== curly braces {} =============== """)
set1 = {1, 2, 'a'}
print(type(set1))  # <class 'set'>
print(set1)        # {1, 2, 'a'}


print(""" Внимание!!! Пустые скобки создают тип данных dict, а не set!!! """)
set2 = {}
print(type(set2))  # <class 'dict'>
print(set2)        # {}


print(""" 2. =============== function set() ===============
IMPORTANT: 
    a.) Must have iterable object!!!
    b.) And every item must be hashable!!!!!
""")

try:
    set(1)
except Exception as e:
    print(f"2.1.{e.__class__.__name__}: {e}")

try:
    set([[1], [2]])
except Exception as e:
    print(f"2.2.{e.__class__.__name__}: {e}")


print(set())       # set()
print(set(""))     # set()
print(set("a"))    # {'a'}
print(set([]))     # set()
print(set(['']))   # {''}
print(set(['a']))  # {'a'}
print(set(['abc']))  # {'abc'}
print(set("abc"))  # {'a', 'b', 'c'}
print()


print(""" 3. =============== set comprehension ===============
IMPORTANT: 
    a.) Must have iterable object!!!
    b.) And every item must be hashable!!!!!
""")

try:
    my_set = {x for x in [[1], [2]]}
except Exception as e:
    print(f"3.2.{e.__class__.__name__}: {e}")

my_set = {x for x in [1, 2, 2, 1, 'a']}
print('\n3.3. my_set =', my_set)
