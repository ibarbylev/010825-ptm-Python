### 1. `isinstance(obj, classinfo)`

**Назначение:** 
* Проверяет, является ли объект `obj` 
  * экземпляром класса `classinfo` 
  * или его подклассов.

**Синтаксис:**

```python
isinstance(obj, classinfo)
```

* `obj` — объект, который проверяем.
* `classinfo` — класс или кортеж классов.

**Примеры:**

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))      # True — это экземпляр Dog
print(isinstance(dog, Animal))   # True — Dog наследует Animal
print(isinstance(dog, int))      # False — это не число

# Можно проверять несколько классов сразу
print(isinstance(dog, (int, Animal, str)))  # True, так как dog — Animal
```

**Особенность**: проверка работает **по всей иерархии наследования**.

---

### 2. `issubclass(class, classinfo)`

**Назначение:** Проверяет, является ли класс `class` **подклассом** `classinfo`.

**Синтаксис:**

```python
issubclass(class, classinfo)
```

* `class` — проверяемый класс.
* `classinfo` — класс или кортеж классов.

**Примеры:**

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))   # True — Dog наследует Animal
print(issubclass(Animal, Dog))   # False — Animal не наследует Dog
print(issubclass(Dog, (int, Animal)))  # True, Dog наследует Animal
```

Отличие от `isinstance`: **проверяет классы, а не объекты**.

---

### 3. Сравнение `isinstance` и `issubclass`

| Функция      | Что проверяет             | Пример                           |
| ------------ | ------------------------- | -------------------------------- |
| `isinstance` | Объект принадлежит классу | `isinstance(dog, Animal)` → True |
| `issubclass` | Класс является подклассом | `issubclass(Dog, Animal)` → True |


