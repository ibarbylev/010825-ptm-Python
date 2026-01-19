## 1. Классификация ошибок `pymongo`

| Ошибка MongoDB                | Описание                                   | Пример ситуации                                           | Пользовательское исключение                 |
| ----------------------------- | ------------------------------------------ | --------------------------------------------------------- | ------------------------------------------- |
| `DuplicateKeyError`           | Нарушение уникальности индекса             | Вставка документа с уже существующим уникальным значением | `class AlreadyExistsError(Exception)`       |
| `WriteError`                  | Общая ошибка записи                        | Некорректные данные для записи                            | `class InvalidDataError(Exception)`         |
| `WriteConcernError`           | Ошибка подтверждения записи                | Некорректные настройки write concern                      | `class WriteConcernFailedError(Exception)`  |
| `OperationFailure`            | Любая ошибка операции                      | Некорректный запрос или команда                           | `class OperationFailedError(Exception)`     |
| `ServerSelectionTimeoutError` | Не удалось подключиться к серверу          | MongoDB недоступен                                        | `class DatabaseUnavailableError(Exception)` |
| `ConfigurationError`          | Ошибка конфигурации клиента                | Некорректный URI или опции клиента                        | `class ConfigurationError(Exception)`       |
| `ConnectionFailure`           | Ошибка соединения                          | Проблемы с сетью или сервером                             | `class ConnectionFailedError(Exception)`    |
| `InvalidDocument`             | Документ не соответствует требованиям BSON | Вставка неподдерживаемого типа данных                     | `class InvalidDocumentError(Exception)`     |

---

## 2. Пример конвертации ошибок в пользовательские исключения

```python
from pymongo import MongoClient, errors

# Пользовательские исключения
class AlreadyExistsError(Exception): 
    pass


class InvalidDataError(Exception): 
    pass


class DatabaseUnavailableError(Exception): 
    pass


class OperationFailedError(Exception): 
    pass


client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["users"]

def insert_user(user):
    try:
        collection.insert_one(user)
    except errors.DuplicateKeyError as e:
        raise AlreadyExistsError("Пользователь уже существует") from e
    except errors.WriteError as e:
        raise InvalidDataError("Неверные данные") from e
    except errors.OperationFailure as e:
        raise OperationFailedError("Ошибка операции в MongoDB") from e
    except errors.ServerSelectionTimeoutError as e:
        raise DatabaseUnavailableError("Сервер MongoDB недоступен") from e
```

Такой подход позволяет:

* Изолировать логику работы с MongoDB от остальной бизнес-логики.
* Обрабатывать конкретные ошибки в приложении в виде своих исключений.

