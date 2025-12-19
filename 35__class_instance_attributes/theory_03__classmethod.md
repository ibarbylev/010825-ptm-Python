## Что такое `@classmethod`?

`@classmethod` — это декоратор, который превращает метод класса в «метод класса», а не объекта.

Главное отличие от обычного метода:
* **первым аргументом получает сам класс** (`cls`), а не объект (`self`).

То есть метод может работать с атрибутами и состоянием **класса**, а не конкретного экземпляра.

---

## Пример: `population` — счётчик созданных экземпляров класса `Person`.

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    
print(Person.get_population())
```

---

## Когда необходимо использовать `@classmethod`?

### 1. Когда нужно создать альтернативный конструктор

Наиболее чАстая причина использования.

```python
from datetime import datetime, date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birthday(cls, name: str, birth_date: datetime):
        """Создание объекта Person по дате рождения (datetime)"""
        today = date.today()
        birthday = birth_date.date()   # Берём только дату

        age = today.year - birthday.year
        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1

        return cls(name, age)

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

alice = Person.from_birthday("Alice", datetime(1990, 1, 1))
bob = Person("Bob", 37)

print(alice)
print(bob)  

# Person(name=Alice, age=35)
# Person(name=Bob, age=37)
```


### 2. Когда метод должен работать с данными класса

См. пример `счётчик созданных экземпляров класса`


### 3. Вопрос "на засыпку":

Почему в класс-методе нельзя просто указать имя класса вместо `cls`?

```python
class Person:
    ...
    
    @classmethod
    def from_birthday(cls, name: str, birth_date: datetime):
        """Создание объекта Person по дате рождения (datetime)"""
        ...
        return Person(name, age)
```