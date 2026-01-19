## Работа с исключениями при использовании специфических драйверов БД

### Постановка проблемы

При работе с базами данных в Python используются различные драйверы
(`mysql-connector-python`, `PyMySQL`, `mysqlclient` и др.).

Каждый из них:

* имеет **собственные классы исключений**;
* по-разному именует иерархию ошибок;
* может быть заменён в процессе развития проекта.

❗ **Проблема** возникает тогда, когда исключения конкретного драйвера
выходят за пределы кода работы с БД и начинают обрабатываться в бизнес-логике приложения.

Это приводит к:

* жёсткой зависимости кода от конкретной библиотеки;
* усложнению сопровождения;
* необходимости переписывать код при смене драйвера.

---

### Примеры специфических исключений каждого из пакетов

| Пакет (для установки)     | Импорт в коде            | Основные/базовые исключения                                                                                                 |
| ------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `PyMySQL`                 | `import pymysql`         | `pymysql.MySQLError` (базовое), есть `IntegrityError`, `OperationalError`, `ProgrammingError`, `InternalError` и др.        |
| `mysql-connector-python`  | `import mysql.connector` | `mysql.connector.Error` (базовое), также есть `DatabaseError`, `IntegrityError`, `ProgrammingError`, `InterfaceError` и др. |
| `mysqlclient` (`MySQLdb`) | `import MySQLdb`         | `MySQLdb.Error` (базовое), есть `DatabaseError`, `IntegrityError`, `OperationalError`, `ProgrammingError` и др.             |

---

### Возможный вариант решения:

```python
from mysql.connector import Error

try:
    fetch_data()
except Error:
    print("Ошибка MySQL")
```

В этом случае:

* внешний код **знает**, какой драйвер используется;
* происходит «утечка» деталей реализации;
* нарушается разделение ответственности.

---

### Улучшенный вариант:

**Идея:**
исключения конкретного драйвера должны обрабатываться *внутри слоя доступа к данным*  
и преобразовываться в **пользовательские (абстрактные) исключения**.

---

### Пример корректной реализации

```python

import mysql.connector
from mysql.connector import Error
from local_settings import dbconfig


class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""
    pass


def fetch_cities(limit: int = 10):
    try:
        with mysql.connector.connect(**dbconfig) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM world.city LIMIT %s",
                    (limit,)
                )
                result = cursor.fetchall()
            
            # Если дошли сюда без исключений — фиксируем транзакцию
            connection.commit()
            return result

    except Error as exc:
        # Откатываем все изменения в случае ошибки
        if connection:
            connection.rollback()
        # Изолируем исключение конкретного драйвера
        raise DatabaseError("Ошибка при работе с базой данных") from exc


if __name__ == "__main__":
    try:
        cities = fetch_cities(10)
        print(*cities, sep="\n")

    except DatabaseError as err:
        print(f"Ошибка приложения: {err}")

```

---

### Пояснение к примеру

#### 1. Пользовательское исключение

```python
class DatabaseError(Exception):
    pass
```

Это **абстрактное исключение**, не связанное с конкретным драйвером.

---

### 2. Оборачивание исключения

```python
except Error as exc:
    raise DatabaseError(...) from exc
```

* драйвер-специфичное исключение **перехватывается**
* наружу выходит только `DatabaseError`
* оригинальная причина сохраняется для логирования и отладки

---

### Вывод:

* **Драйвер-специфичные исключения "не выпускаются" за пределы слоя доступа к данным.**

Иначе говоря:

* бизнес-логика **не знает**, какой драйвер используется;
* код становится устойчивым к замене библиотеки;
* архитектура остаётся чистой и поддерживаемой.

Это один из базовых принципов построения надёжных и масштабируемых приложений.
