### 3. LSP: Liskov Substitution Principle (принцип подстановки Лисковой)

***Объекты дочерних классов должны полностью сохранять поведение базового класса.***

Иными словами: все атрибуты и методы родительского класса должны работать и в дочернем.

Таким образом, LSP помогает создавать **устойчивую и предсказуемую иерархию классов**.

---

### Пример нарушения принципа LSP:

```python
class Bird:
    def fly(self):
        print("I can fly!")

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("I cannot fly!")

# Использование
def make_bird_fly(bird: Bird):
    bird.fly()

bird = Bird()
ostrich = Ostrich()

make_bird_fly(bird)     # I can fly!
make_bird_fly(ostrich)  # Ошибка! Нарушение LSP
```

Проблема: 
* `Ostrich` наследует `Bird`, 
* но не может выполнить метод `fly()`, который ожидался у всех птиц. 

Любой код, который использует базовый класс `Bird`, ломается при подстановке `Ostrich`.

---

**Применение LSP (разделение интерфейсов):**

```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly!")

class Ostrich(Bird):
    def run(self):
        print("I can run!")

# Использование
def make_bird_fly(bird: FlyingBird):
    bird.fly()

sparrow = FlyingBird()
ostrich = Ostrich()

make_bird_fly(sparrow)  # I can fly!
# make_bird_fly(ostrich) теперь невозможно вызвать, LSP соблюден
```

Теперь:

* `FlyingBird` реализует `fly()`.
* `Ostrich` не наследует `FlyingBird`, а только `Bird`.
* Код, который ожидает летать, больше не ломается.

