## 1. Что такое JSON

**JSON (JavaScript Object Notation)** — это текстовый формат для хранения и обмена данными.  
Он похож на словари Python:

* Объекты JSON ↔ словари Python (`dict`)
* Массивы JSON ↔ списки Python (`list`)
* Строки, числа, булевы значения и `null` ↔ строки, числа, `True/False`, `None` в Python

**Пример JSON:**

```json
{
  "name": "Alice",
  "age": 30,
  "is_student": false,
  "courses": ["Math", "Physics"],
  "is_active": true
}
```

---

## 2. Модуль `json` в Python

Python имеет встроенный модуль `json`, который позволяет:

1. **Парсить JSON в Python объекты (Десериализация)** (`json.loads`, `json.load`)
2. **Конвертировать Python объекты в JSON (Сериализация)** (`json.dumps`, `json.dump`)

---

## 3. Основные функции модуля

### 3.1 Десериализация: преобразование JSON в Python (`load` и `loads`)

* `json.loads()` — преобразует JSON-строку в Python-объект
* `json.load()` — считывает JSON из файла и преобразует в Python-объект

```python
import json

json_string = '{"name": "Alice", "age": 30, "is_student": false}'
data = json.loads(json_string)  # str -> dict
print(data)
print(data['name'])
```

Для чтения из файла:

```python
with open("data.json", "r") as f:
    data = json.load(f)
```

---

### 3.2 Сериализация: преобразование Python в JSON (`dump` и `dumps`)

* `json.dumps()` — конвертирует Python-объект в JSON-строку
* `json.dump()` — записывает Python-объект в файл в формате JSON

```python
import json

data = {
    "name": "Bob",
    "age": 25,
    "is_student": True,
    "courses": ["Biology", "Chemistry"]
}

# В строку
json_string = json.dumps(data, indent=4)
print(json_string)

# В файл
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)
```

> Параметр `indent` делает JSON читаемым с отступами.

---

### 3.3 Настройка сериализации

`json.dumps()` позволяет контролировать формат:

* `indent=4` — отступ для читаемого вида
* `sort_keys=True` — сортировка ключей в алфавитном порядке
* `ensure_ascii=False` — позволяет выводить Unicode символы (например, кириллицу) без экранирования

```python
json_string = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
print(json_string)
```

---

### 3.4 Дополнительные параметры сериализации

Функция `json.dumps()` поддерживает ряд полезных параметров, которые позволяют настроить формат вывода JSON:

* `indent` — задаёт отступ для читаемого вида.
  Пример:

```python
import json

data = {"name": "Bob", "age": 25, "courses": ["Biology", "Chemistry"]}

json_string = json.dumps(data, indent=4)
print(json_string)
```

Вывод будет красиво структурирован с отступами:

```json
{
    "name": "Bob",
    "age": 25,
    "courses": [
        "Biology",
        "Chemistry"
    ]
}
```
Альтернатива (без indent):

```json
{"name": "Bob", "age": 25, "courses": ["Biology", "Chemistry"]}
```

---

* `sort_keys` — сортирует ключи словаря в алфавитном порядке:

```python
json_string = json.dumps(data, sort_keys=True)
print(json_string)
```

```json
{"age": 25, "courses": ["Biology", "Chemistry"], "name": "Bob"}
```

Вместо:

```json
{"name": "Bob", "age": 25, "courses": ["Biology", "Chemistry"]}
```

---

* `ensure_ascii` — управляет кодировкой символов Unicode:

  * `True` (по умолчанию) — все не-ASCII символы будут экранироваться `\uXXXX`.
  * `False` — символы будут выводиться как есть (например, кириллица).

```python
data = {"name": "Алиса", "age": 30}
json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)
```

Вывод:

```json
{"name": "Алиса", "age": 30}
```

Вместо:

```json
{"name": "\u0410\u043b\u0438\u0441\u0430", "age": 30}
```

---

* `default` — позволяет сериализовать объекты, которые стандартно не поддерживаются (например, `datetime`):


---

### 3.5 Обработка нестандартных объектов

По умолчанию `json` умеет работать только с базовыми типами (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`).
Если нужно сериализовать объект класса, можно использовать `default`:

```python
import json
from datetime import datetime

data = {"event": "meeting", "time": datetime.now()}

json_string = json.dumps(data, default=str)
print(json_string)
```

Вывод:

```json
{"event": "meeting", "time": "2025-11-20 17:54:32.908556"}
```

Иначе — ошибка:

```json
  File "/usr/lib/python3.12/json/encoder.py", line 180, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type datetime is not JSON serializable
```


---

### 3.6 Разбор JSON с ошибками

* Если JSON некорректный, `json.loads()` выбросит `json.JSONDecodeError`.
* Можно обернуть в `try/except` для безопасного разбора:

```python
try:
    data = json.loads('{"name": "Alice", "age": }')
except json.JSONDecodeError as e:
    print("Ошибка JSON:", e)

# Ошибка JSON: Expecting value: line 1 column 26 (char 25)
```

---

## 4. Практическое использование

* Обмен данными с веб-API (REST API часто возвращает JSON)
* Сохранение настроек приложения
* Кеширование данных в файлах
* Логирование структурированных данных

