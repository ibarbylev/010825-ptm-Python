## `strip()`, `lstrip()`, `rstrip()`



| Метод      | Что делает                                            | Пример                              |
| ---------- | ----------------------------------------------------- |-------------------------------------|
| `strip()`  | Убирает указанные символы **с начала и конца строки** | `"  hello  ".strip()  # "hello"`    |
| `lstrip()` | Убирает указанные символы **только слева**            | `"  hello  ".lstrip()  # "hello  "` |
| `rstrip()` | Убирает указанные символы **только справа**           | `"  hello  ".rstrip()  # "  hello"` |

---

## Примеры

### 1 Обычное удаление пробелов

```python
text = "   Python   "
print(text.strip())   # "Python"
print(text.lstrip())  # "Python   "
print(text.rstrip())  # "   Python"
```

### 2 Удаление конкретных символов

```python
text = "///hello///"
print(text.strip("/"))   # "hello"
print(text.lstrip("/"))  # "hello///"
print(text.rstrip("/"))  # "///hello"
```

### 3. Удаление нескольких символов

```python
text = ".,!hello!.,"
print(text.strip(".,!"))  # "hello"
```

**ВАЖНО**: Символы удаляются ДО ПЕРВОГО символа НЕ ИЗ указанного набора символов:  


```python
text = "abcdeabc"
print(text.strip("ac"))  # "bcdeab"  (удаляет все `a` и `c` с концов, не внутри)
```
