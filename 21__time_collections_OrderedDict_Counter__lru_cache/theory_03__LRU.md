## Что такое LRU cache?

LRU (Least Recently Used) — это стратегия, при которой из кэша удаляются  
наименее недавно использованные элементы, когда кэш заполняется.


### Пример, создания LRU кэша с помощью OrderedDict:

```python
from collections import OrderedDict

cache = OrderedDict()
MAX_SIZE = 3

def put(key, value):
    # если ключ уже есть — удаляем его, чтобы потом вставить как "новый"
    if key in cache:
        cache.pop(key)
    cache[key] = value  # вставляем в конец (новый элемент)
    # если переполнен — удаляем самый старый (первый)
    if len(cache) > MAX_SIZE:
        cache.popitem(last=False)

    print(cache)  # просто показываем текущее состояние

# наполняем кэш
put('a', 1)
put('b', 2)
put('c', 3)
put('a', 1)  # "a" снова используется → переносим в конец
put('d', 4)  # переполнение → удалится "b"

# OrderedDict({'a': 1})
# OrderedDict({'a': 1, 'b': 2})
# OrderedDict({'a': 1, 'b': 2, 'c': 3})
# OrderedDict({'b': 2, 'c': 3, 'a': 1})
# OrderedDict({'c': 3, 'a': 1, 'd': 4})
```