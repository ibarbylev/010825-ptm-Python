### Метод `__bool__`

Магический метод `__bool__` отвечает за булево значение объекта (`True` или `False`)
при использовании его в логическом контексте: `if`, `while`, `not` и других булевых выражениях.

---

**Синтаксис**

```python
class MyClass:
    def __bool__(self):
        # вернуть True или False
        return True  # или False
```

---

### Пример

```python
class Box:
    def __init__(self, items):
        self.items = items
    
    def __bool__(self):
        # объект пустой → False, есть элементы → True
        return bool(self.items)


empty_box = Box([])
full_box = Box([1, 2, 3])

print(bool(empty_box))  # False
print(bool(full_box))   # True

if full_box:
    print("Коробка не пуста!")


# False
# True
# Коробка не пуста!
```

---

### Альтернатива `__bool__`

Если `__bool__` не определён, Python использует `__len__`:

```python
class MyObject:
   def __init__(self, data):
       self.data = data
   def __len__(self):
       return len(self.data)


o1 = MyObject('asdf')
print(bool(o1))
# True

o2 = MyObject('')
print(bool(o2))
# False
```

