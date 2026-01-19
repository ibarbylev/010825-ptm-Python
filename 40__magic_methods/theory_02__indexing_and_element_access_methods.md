## Методы индексации и доступа к элементам

### 1. `__getitem__(self, key)`

Используется для чтения элемента:

```python
obj[key]
```

**Пример:**

```python
class Vector:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

v = Vector([10, 20, 30])
print(v[1])  # 20
```

Метод поддерживает индексы, slicing и любые ключи.

---

### 2. `__setitem__(self, key, value)`

Используется для присваивания:

```python
obj[key] = value
```

**Пример:**

```python
def __setitem__(self, index, value):
    self.data[index] = value
```

---

### 3. `__delitem__(self, key)`

Удаляет элемент:

```python
del obj[key]
```

**Пример:**

```python
def __delitem__(self, index):
    del self.data[index]
```

---

### 4. `__len__(self)`

Возвращает длину объекта:

```python
len(obj)
```

**Пример:**

```python
def __len__(self):
    return len(self.data)
```

---

### 5. `__contains__(self, item)`

Отвечает за оператор `in`:

```python
item in obj
```

Если не определён, Python перебирает элементы.

---

### 6. Срезы — `slice` в `__getitem__`

Если поступает срез, Python передаёт объект `slice(start, stop, step)`.

```python
def __getitem__(self, key):
    if isinstance(key, slice):
        return Vector(self.data[key])
    return self.data[key]
```

---

### Резюме

| Метод          | Использование               |
| -------------- | --------------------------- |
| `__getitem__`  | чтение элемента: `obj[key]` |
| `__setitem__`  | запись: `obj[key] = x`      |
| `__delitem__`  | удаление: `del obj[key]`    |
| `__contains__` | проверка `in`               |
| `__len__`      | длина `len(obj)`            |
| `__iter__`     | итерация `for x in obj`     |


