## Вложенные классы

**Вложенный класс** — это класс, определённый *внутри другого класса*.

Он НЕ существует самостоятельно, а только как **атрибут** внешнего класса.

```python
class Human:
    class Heart:
        def beat(self):
            return "Тук-тук"

h = Human()
heart = Human.Heart()
print(heart.beat())  # Тук-тук


try:
    heart2 = Heart()
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
    # NameError: name 'Heart' is not defined
```

Как видно из примера, вложенный класс невозможно вызвать без упоминания внешнего.

Вложенный класс — это разновидность композиции.  
С той только разницей, в отличие от обычной композиции,  
вложенный класс в принципе невозможно создать без внешнего.


### Схема трёх вариантов отношения объектов:

```
        НАСЛЕДОВАНИЕ               КОМПОЗИЦИЯ                            АГРЕГАЦИЯ 
          (is-a)               (has-a, часть целого)            (has-a, независимый компонент)
             ^          
             |
     +----------------+         +-----------------+         +-----------------+       +--------------+
     |      Dog       |         |       Car       |         |                 |       |              |
     +----------------+         |  +-----------+  |         |    Employee     |-------|  Department  |
             |                  |  |           |  |         |                 |       |              |
             v                  |  |  Engine   |  |         +-----------------+       +--------------+
     +----------------+         |  |           |  |         
     |     Animal     |         |  +-----------+  |
     +----------------+         +-----------------+ 

                                     КОМПОЗИЦИЯ
                                          |
                                          v
                                +-----------------+
                                |     Car         |
                                |  class Engine   |  ← вложенный класс (часть Car)
                                +-----------------+

```

Внешний класс используют для логической группировки вспомогательных структур,   
которые не имеют смысла вне контекста внешнего класса.

Или, чтобы не засорять пространство имён на уровне внешнего класса объектами,  
которые нужны ИСКЛЮЧИТЕЛЬНО внутри внешнего класса.

---

⚠️
Важная особенность вложенных классов Python

### Нет неявной связи с экземпляром внешнего класса

(В отличие от Java / Kotlin)

Чтобы передать данные внешнего объекта — нужно делать это явно.

```python
class Outer:
    def __init__(self, value):
        self.value = value

    class Inner:
        def print_outer_value(self):
            print(self.value)      # ❌ Ошибка: 'Inner' не знает про self внешнего класса


o = Outer(10)
i = Outer.Inner()
try:
    i.print_outer_value()
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')

```

Сделать это можно только явно:

```python
class Outer:
    def __init__(self, value):
        self.value = value

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def print_outer_value(self):
            print(self.outer.value)


o = Outer(10)
i = Outer.Inner(o)      # ← передали связь вручную
i.print_outer_value()   # → 10

```

### Но с атрибутами класса (в отличие от атрибутов экземпляров класса) связь есть

```python
class Outer:
    class_attr = 100   # атрибут КЛАССА

    class Inner:
        def show_outer_class_attr(self):
            print(Outer.class_attr)   # ✔ доступ есть

i = Outer.Inner()
i.show_outer_class_attr()
```