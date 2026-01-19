## 4 столпа (кита, основы) ООП

### 1. Инкапсуляция (Encapsulation)

**Смысл:** 
1. Скрытие внутренней реализации объекта и 
2. предоставление доступа к данным через методы.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)    # Ошибка! Доступ запрещён
```

> Здесь баланс скрыт, и доступ к нему идёт только через методы класса.

---

### 2. Абстракция (Abstraction)

**Смысл:** 
* Отделение сути объекта от деталей реализации. 
* Мы работаем с объектом через его интерфейс, не заботясь о его внутренней "кухне".

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # 78.5
```

> Мы знаем, что у фигуры есть метод `area`, не вдаваясь в формулу для круга или квадрата.

---

### 3. Наследование (Inheritance)

**Смысл:** 
* Позволяет создавать новый класс на основе существующего, 
* наследуя его свойства и методы.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} едет")

class Car(Vehicle):
    def honk(self):
        print("Биб-бип!")

my_car = Car("Toyota")
my_car.drive()  # Toyota едет
my_car.honk()   # Биб-бип!
```

> `Car` наследует метод `drive` от `Vehicle`, а также добавляет свой собственный `honk`.

---

### 4. Полиморфизм (Polymorphism)

**Смысл:** 
* Способность объектов разных классов использовать один и тот же интерфейс по-разному.

```python
class Cat:
    def sound(self):
        print("Мяу")

class Dog:
    def sound(self):
        print("Гав")

animals = [Cat(), Dog()]
for animal in animals:
    animal.sound()  # Мяу, Гав
```

> Метод `sound()` одинаковый по имени, но работает по-разному для кошки и собаки.

---

✅ **Итого:**

* **Инкапсуляция** — скрываем детали (private атрибуты).
* **Абстракция** — создаём интерфейс (abstract class).
* **Наследование** — переиспользуем код родителя (child class).
* **Полиморфизм** — разные реализации одного интерфейса (один метод — разные результаты).


