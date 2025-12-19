## 1. Базовые типы

```python
name: str
age: int
price: float
active: bool
data: bytes
```

---

## 2. Коллекции

```python
numbers: list[int]
names: set[str]
user_ids: frozenset[int]
options: dict[str, int]
pairs: tuple[str, int]
```

> 🔹 До Python 3.9 приходилось писать `List[int]`, `Dict[str, int]`, `Tuple[str, int]` через модуль `typing`.

---

## 3. Вложенные структуры

```python
matrix: list[list[int]]
config: dict[str, list[tuple[str, int]]]
```

ВАЖНО: Вложенные структуры усложняют читаемость кода.  
Поэтому указывать вложенный тип желательно, но совсем не обязательно

---

## 4. Опциональные и объединённые типы (Python 3.10+)

### Старый синтаксис (до 3.10):

```python
from typing import Optional, Union

id: Optional[int]  # то же самое, что Union[int, None]
value: Union[int, str]
```

### Новый синтаксис (3.10+):

```python
id: int | None
value: int | str
```

