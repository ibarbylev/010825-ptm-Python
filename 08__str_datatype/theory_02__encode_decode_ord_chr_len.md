### 1. `encode()`

Метод `encode()` используется для преобразования строки (`str`) в байты (`bytes`)  
с использованием определённой кодировки (обычно UTF-8).

**Синтаксис:**

```python
string.encode(encoding="utf-8", errors="strict")
```

* `encoding` — кодировка (по умолчанию `utf-8`).
* `errors` — как обрабатывать ошибки (`strict`, `ignore`, `replace`).

**Пример:**

```python
text = "Привет"
encoded_text = text.encode("utf-8")
print(encoded_text)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
```

Теперь `encoded_text` — это байтовая строка (`bytes`).

---

### 2. `decode()`

Метод `decode()` применяется к байтам (`bytes`), чтобы снова получить строку (`str`).

**Пример:**

```python
decoded_text = encoded_text.decode("utf-8")
print(decoded_text)  # Привет
```

---

### 3. `ord()`

Функция `ord()` возвращает Unicode-код (число) для символа.

**Пример:**

```python
print(ord("A"))  # 65
print(ord("я"))  # 1103
```

---

### 4. `chr()`

Функция `chr()` делает обратное — из кода возвращает символ.

**Пример:**

```python
print(chr(65))    # A
print(chr(1103))  # я
```

---

### 5. `len()`

Функция `len()` возвращает длину объекта: строки, списка, словаря и т. д.

**Пример:**

```python
text = "Привет"
print(len(text))  # 6 (количество символов)
```

Но если считать байты:

```python
print(len(text.encode("utf-8")))  # 12 (UTF-8 кодирует кириллицу в 2 байта)
```
