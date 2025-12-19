### 1. Недостатки предыдущего примера


```python
from typing import Iterable, Iterator

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # обновляет значение старта при перезапуске с помощью iter()
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Конец итерации
        value = self.current
        self.current += 1
        return value


my_range = MyRange(1, 5)
print(isinstance(my_range, Iterable))
print(isinstance(my_range, Iterator))


for number in my_range:
    print(number)

```

Экземпляр класса `MaRange` является итератором, так как содержит методы `__iter__()` и `__next__()`.

Но это нарушает **принцип разделение ответственности**, когда объект одновременно представляет собой
* и набор данных 
  * (должен быть итерируемым и создавать новые итераторы)
* и процесс обхода 
  * (должен быть итератором и не должен перезапускаться)  



### 2. Улучшенный вариант итератора

Разделяем между собой `Iterator` и `Iterable`:

```python
from typing import Iterable, Iterator

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.start, self.end)


class MyRangeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Конец итерации
        value = self.current
        self.current += 1
        return value


my_range = MyRange(1, 5)
print(isinstance(my_range, Iterable))  # True
print(isinstance(my_range, Iterator))  # False

my_range_iter = iter(my_range)
print(isinstance(my_range_iter, Iterable))  # True
print(isinstance(my_range_iter, Iterator))  # True

while True:
    try:
        print(next(my_range_iter))
    except StopIteration:
        print("Done!")
        break
```
