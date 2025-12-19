### Методы сравнения в Python

Чтобы объекты пользовательского класса можно было сравнивать, нужно определить специальные методы:

| Оператор | Спецметод             | Значение         |
| -------- | --------------------- | ---------------- |
| `<`      | `__lt__(self, other)` | меньше           |
| `<=`     | `__le__(self, other)` | меньше или равно |
| `>`      | `__gt__(self, other)` | больше           |
| `>=`     | `__ge__(self, other)` | больше или равно |
| `==`     | `__eq__(self, other)` | равно            |
| `!=`     | `__ne__(self, other)` | не равно         |

---

### Декоратор `@functools.total_ordering`

* Если добавить в класс декоратор `@functools.total_ordering`
* то достаточно реализовать один метод `__eq__`
* и один любой метод сравнения (`__lt__`, `__le__`, `__gt__`, `__ge__`).

Остальные 4 метода "добавит" сам декоратор.

---

#### Пример

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


p1 = Person(30)
p2 = Person(25)

print(p1 > p2)   # True
print(p1 <= p2)  # False
print(p1 == p2)  # False
```

Мы реализовали только:

* `__eq__`
* `__lt__`

Остальные (`>`, `>=`, `<=`) создал `total_ordering`.

---

### Исключение `NotImplemented`

Использование **`NotImplemented`** в методах сравнения — важная часть правильной pythonic реализации.

`NotImplemented` — это специальное значение (не исключение!), которое говорит интерпретатору:

> «Я не знаю, как сравнивать себя с этим объектом — попробуй другой операнд».

Когда метод возвращает `NotImplemented`, Python пытается вызвать **обратный метод** у другого объекта:

* Для `<` → вызывает `other.__gt__(self)`
* Для `<=` → вызывает `other.__ge__(self)`
* Для `==` → вызывает `other.__eq__(self)`
* и так далее.

Если *оба* возвращают `NotImplemented`, Python выдаёт `TypeError`.

---

### Когда нужно возвращать `NotImplemented`?

**Когда другой объект не того типа, который класс умеет сравнивать.**

Обычно — если `other` не относится к текущему классу.

---

### Корректное использование `NotImplemented`

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
```

Почему правильно возвращать исключение. а не "выбрасывать" ошибку?

* Если сравнить `Person()` с `42`, Python поймёт, что данное сравнение невозможно.
* и попробует применить альтернативный метода (который может быть реализован)
* Если вместо `return NotImplemented` использовать `raise TypeError("Can't compare")`, то это
  * ломает обратный вызов (`other.__gt__`) 
  * и нарушает поведение Python.
