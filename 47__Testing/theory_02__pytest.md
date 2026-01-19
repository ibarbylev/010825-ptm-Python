
## 1. Что такое `pytest`

`pytest` — это **популярный внешний фреймворк тестирования** для Python.

Он позволяет:

* писать **лаконичные** и читаемые тесты;
* использовать обычный `assert`;
* легко работать с фикстурами;
* тестировать `async`-код;
* получать понятные отчёты об ошибках;
* масштабировать тесты под большие проекты.

**Установка:**

```bash
pip install pytest
```

---

## 2. Основные понятия

### Тест в `pytest`

Тест — это **обычная функция**, которая:

* начинается с `test_`
* содержит `assert`

```python
def test_example():
    assert 1 + 1 == 2
```

Тесты должны быть:

* **независимыми**
* **повторяемыми**
* **автоматическими**

(ровно как и в `unittest`)

---

## 3. Структура теста (AAA)

`pytest` также следует паттерну **AAA**:

1. **Arrange** — подготовка данных
2. **Act** — вызов тестируемого кода
3. **Assert** — проверка результата

```python
def test_multiply_by_2():
    # Arrange
    x = 2

    # Act
    result = multiply_2(x)

    # Assert
    assert result == 4
```

---

## 4. Базовая структура `pytest`

```python
def multiply_2(x):
    return 2 * x


def test_multiply_2_returns_double():
    result = multiply_2(3)
    assert result == 6
```

### Обязательные элементы:

* имя файла: `test_*.py` или `*_test.py`
* имя функции: `test_*`
* проверка через обычный `assert`

❗ **Классы не обязательны**

---

## 5. Assert в `pytest`

Используется **обычный `assert`**, но с улучшенной диагностикой:

```python
def test_list_contains_value():
    data = [1, 2, 3]
    assert 2 in data
```

При падении pytest покажет:

```text
assert 2 in [1, 3]
```

Можно проверять исключения:

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

---

## 6. Фикстуры (`fixtures`)

Фикстуры — это **замена `setUp / tearDown`**, но намного мощнее.

```python
import pytest

@pytest.fixture
def data():
    return [1, 2, 3]


def test_data_length(data):
    assert len(data) == 3
```

### Особенности фикстур:

* внедряются как аргументы функции
* могут переиспользоваться
* имеют области видимости (`scope`)

---

## 7. Область видимости фикстур

```python
@pytest.fixture(scope="function")  # по умолчанию
@pytest.fixture(scope="class")
@pytest.fixture(scope="module")
@pytest.fixture(scope="session")
```

Пример:

```python
@pytest.fixture(scope="module")
def db_connection():
    print("connect")
    yield
    print("disconnect")
```

---

## 8. Параметризация тестов

Позволяет запускать **один тест с разными данными**:

```python
import pytest

@pytest.mark.parametrize(
    "x, expected",
    [
        (2, 4),
        (3, 6),
        (5, 10),
    ]
)
def test_multiply_2(x, expected):
    assert multiply_2(x) == expected
```

---

## 9. Запуск тестов

### Запуск всех тестов:

```bash
pytest
```

### Запуск конкретного файла:

```bash
pytest test_math.py
```

### Запуск с подробным выводом:

```bash
pytest -v
```

### Остановиться при первой ошибке:

```bash
pytest -x
```

---

## 10. Организация тестов

Для больших проектов удобно создать файл `pytest.ini` в корне проекта:

```
project/
│
├── main.py
├── pytest.ini
└── tests/
    ├── test_main.py
    └── test_utils.py
```

Пример `pytest.ini`:

```ini
[pytest]
# Автопоиск тестов в папке tests
testpaths = tests
# Шаблоны имен файлов
python_files = test_*.py *_test.py
# Шаблоны имен функций
python_functions = test_*
# Уровень подробности вывода
addopts = -v
```

После этого можно просто запускать:

```bash
pytest
```

pytest **сам найдёт тесты** и покажет детальный отчёт.


---

## 11. Классы в `pytest` (необязательно)

Иногда используются для логической группировки:

```python
class TestMath:

    def test_add(self):
        assert 1 + 1 == 2

    def test_sub(self):
        assert 2 - 1 == 1
```

❗ Нельзя использовать `__init__`

---

## 12. Async-тесты

`pytest` отлично работает с `async`:

```python
import pytest

@pytest.mark.asyncio
async def test_async_func():
    result = await async_func()
    assert result == 42
```

---

## 13. Пример использования `pytest.raises`

```python
import pytest

def divide(x, y):
    return x / y

def test_divide_zero():
    # Проверяем, что возникает ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

* Контекстный менеджер `pytest.raises(Exception)` ловит исключение
* Можно также проверить сообщение или свойства исключения:

```python
def test_divide_zero_message():
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(5, 0)
    assert "division by zero" in str(exc_info.value)
```

---

## 14. Пример использования `unittest.mock`

```python
import sys
from unittest.mock import patch

def get_argv_second_element():
    return sys.argv[1]

def test_mock_sys_argv():
    with patch.object(sys, 'argv', ['script.py', 'mocked']):
        assert get_argv_second_element() == 'mocked'
```

* `patch.object` временно заменяет атрибут объекта
* После выхода из блока значение **восстанавливается автоматически**

---

## 15. Хорошие практики pytest

✔️ Один тест — одна логическая проверка  
✔️ Имена тестов описывают поведение  
✔️ Использовать фикстуры вместо `setUp`  
✔️ Параметризация вместо повторения  
❌ Не писать логику в тестах  
❌ Не зависеть от порядка выполнения  

---

## 16. Сравнение `unittest` и `pytest`

| unittest               | pytest                     |
| ---------------------- |----------------------------|
| встроенный             | внешний (нужна установка)  |
| много шаблонного кода  | минимализм                 |
| классы обязательны     | функции — по умолчанию     |
| assert-методы          | обычный `assert`           |
| слабая async-поддержка | **полная async-поддержка** |
| setUp / tearDown       | fixtures                   |

