# Сортировка словарей

До версии Python 3.7 сам термин сортировки словарей отсутствовал!

Теперь можно, правда, с оговорками (в сложных сортировках может дать неожиданный результат).

Поэтому, для сложных и ответственных сортировок используйте `OrderedDict` (упорядоченный словарь)

## Алгоритм сортировки словаря

1. "Разбираем" словари на список пар ключ-значение
2. Сортируем этот список с помощью `sorted()`
3. Превращаем результат в словарь с помощью  `dict()` 

### Пример 1
Сортировка по ключу (по возрастанию)

```python
d = {"name": "Alice", "age": 25, "city": "Paris"}

# 1. "Разбираем" словари на список пар ключ-значение
list_of_pairs = list(d.items())
print(list_of_pairs) # [('name', 'Alice'), ('age', 25), ('city', 'Paris')]

# 2. Сортируем этот список с помощью `sorted()`  
sorted_list = sorted(list_of_pairs)
print(sorted_list)  # [('age', 25), ('city', 'Paris'), ('name', 'Alice')]

# 3. Превращаем результат в словарь с помощью  `dict()`
new_dict = dict(sorted_list)
print(new_dict)
# {'age': 25, 'city': 'Paris', 'name': 'Alice'}
```

### Пример 1.1.
Объект `dict_items` тоже сортируется, поэтому решение можно упростить (совместить этапы):

```python
d = {"name": "Alice", "age": 25, "city": "Paris"}

new_dict = dict(sorted(d.items()))
print(new_dict)
# {'age': 25, 'city': 'Paris', 'name': 'Alice'}
```

### Пример 2
Сортировка по значению (по возрастанию)

```python
d = {"name": "Alice", "age": 25, "city": "Paris"}

# 1. "Разбираем" словари на список пар ключ-значение
list_of_pairs = list(d.items())
print(list_of_pairs) # [('name', 'Alice'), ('age', 25), ('city', 'Paris')]

# 2. Сортируем этот список с помощью `sorted()`  
sorted_list = sorted(list_of_pairs, key=lambda x: str(x[1]))
print(sorted_list)  # [('age', 25), ('city', 'Paris'), ('name', 'Alice')]

# 3. Превращаем результат в словарь с помощью  `dict()`
new_dict = dict(sorted_list)
print(new_dict)
# {'age': 25, 'city': 'Paris', 'name': 'Alice'}
```

## Алгоритм реверса работает так же

Разница только в функции на втором этапе: вместо `sorted()` используют `reversed()`.

```python
d = {"name": "Alice", "age": 25, "city": "Paris"}

new_dict = dict(reversed(d.items()))
print(new_dict)
# {'city': 'Paris', 'age': 25, 'name': 'Alice'}
```