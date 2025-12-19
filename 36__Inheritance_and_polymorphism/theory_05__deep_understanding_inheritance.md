### Почему Student не считает свои объекты?

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        self.__class__.population += 1

    @classmethod
    def get_population(cls):
        return cls.population


class Student(Person):
    pass


p1 = Person("John")
p2 = Person("Mary") 
s1 = Student("Peter")
print(Student.population)   # 3
```

Мы наследовали в классе Student все атрибуты и методы класса Person.

Тем не менее у Student `population` работает "неправильно":
* почему-то сосчитал и свои объекты, и объекта класса-родителя.

1. Неужели атрибуты класса не передаются по наследству (в отличие от методов)?
   * (Или же здесь какая-то иная причина?)

2. Как изменить код, чтобы атрибут класса Student `population` заработал-таки правильно?