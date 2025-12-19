### Метод `__call__`

Магический метод `__call__` в Python позволяет сделать объект вызываемым как функцию.  

Иными словами этот метод придаёт объекту свойства функции

---

**Синтаксис**

```python
class MyCallable:
    def __call__(self, *args, **kwargs):
        # код, который выполняется при вызове объекта
        print("Вызов объекта с аргументами:", args, kwargs)
```

---

### Пример

```python
class Adder:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n + x

add_five = Adder(5)
print(add_five(10))  # 15
print(add_five(3))   # 8
```

В этом примере:

* `add_five(10)` эквивалентно `add_five.__call__(10)`
* Объект хранит состояние `n = 5`, которое используется при каждом вызове

