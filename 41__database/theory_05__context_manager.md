## Работа с MySQL через контекстный менеджер в Python

Подключение, когда объекты соединения и курсора создавались вручную, а затем закрывались через `close()`, 
имеет ряд существенных недостатков:

* если внутри запроса возникает ошибка, 
  * соединение и/или курсор могут остаться открытыми,
  * что приведёт к утечке ресурсов.
* программист может банально забыть добавить `close()` в одном из подключений.

Решение проблемы — **Контекстный менеджер**:

---

### 1. Контекстный менеджер

```python
import mysql.connector
from local_settings import dbconfig

# Контекстный менеджер для соединения и курсора
with mysql.connector.connect(**dbconfig) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM world.city LIMIT 10")
        print(*cursor.fetchall(), sep="\n")
```

**Пояснения:**

* `with mysql.connector.connect(**dbconfig) as connection:`
  Соединение автоматически закроется после выхода из блока `with`.

* `with connection.cursor() as cursor:`
  Курсор также закроется автоматически.

**Плюсы такого подхода по сравнению с простейшим подключением:**

1. **Безопасность и надёжность** — даже при возникновении исключения ресурсы будут освобождены.
2. **Чистый и читаемый код** — сразу видно границы работы с соединением и курсором.

**Минусы:**

* Если нужен более сложный контроль (например, логирование, автоматический commit/rollback), 
  * стандартный `with` не позволяет легко это расширить.

---

## 2. Создание собственного класса-контекстного менеджера

```python
import mysql.connector

class MySQLConnection:
    def __init__(self, db_config):
        self.dbconfig = db_config
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.dbconfig)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
```

Использование:

```python
from local_settings import dbconfig

with MySQLConnection(dbconfig) as db:
    db.cursor.execute("SELECT * FROM world.city LIMIT 10")
    print(*db.cursor.fetchall(), sep="\n")
```

Здесь в dunder-методах `__enter__()` и `__exit__()` 
* мы определяем поведение контекстного менеджера
* и при необходимости можем существенно расширить его возможности.

**Плюсы собственного класса:**

1. **Автоматическое закрытие ресурсов** — так же, как у стандартного `with`.
2. **Возможность расширения** — легко добавить автоматический commit/rollback, логирование, обработку ошибок.
3. **Инкапсуляция соединения** — блок кода становится более объектно-ориентированным.

**Минусы:**

* Требуется немного больше кода, чем при стандартном `with`.
* Без дополнительной логики класс сам по себе не даёт преимуществ кроме читаемости и безопасности.

---

### Вывод

Использование контекстного менеджера при работе с MySQL:

* Делает код безопаснее и читаемее.
* Исключает необходимость вручную закрывать соединение и курсор.
* Позволяет создавать собственные обёртки для расширенного функционала.

