# Пример: несколько конфигураторов для разных частей приложения

## `log_config.py`

```python
import logging

# --- Общий формат ---
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] (%(name)s): %(message)s"
)

# --- Конфиг для основного приложения ("app") ---
file_handler_main = logging.FileHandler("main.log", encoding="utf-8")
file_handler_main.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

app_logger = logging.getLogger("app")
app_logger.setLevel(logging.INFO)
app_logger.handlers.clear()
app_logger.addHandler(file_handler_main)
app_logger.addHandler(console_handler)


# --- Конфиг для базы данных ("db") ---
file_handler_db = logging.FileHandler("db.log", encoding="utf-8")
file_handler_db.setFormatter(formatter)

db_logger = logging.getLogger("db")
db_logger.setLevel(logging.DEBUG)
db_logger.handlers.clear()
db_logger.addHandler(file_handler_db)


# --- Конфиг для сетевых операций ("network")---
file_handler_net = logging.FileHandler("network.log", encoding="utf-8")
file_handler_net.setFormatter(formatter)

net_logger = logging.getLogger("network")
net_logger.setLevel(logging.WARNING)
net_logger.handlers.clear()
net_logger.addHandler(file_handler_net)


# Проверим
if __name__ == "__main__":
    app_logger.info("Сообщение из основного логгера")
    db_logger.debug("Сообщение из логгера базы данных")
    net_logger.error("Ошибка из сетевого логгера")
```

---

## Как использовать в других модулях

`main.py`

```python
import logging
import log_config  # ← подключает все логгеры

log = logging.getLogger("app")
log.info("Привет из основного модуля")
```

`database.py`

```python
import logging
import log_config

db_log = logging.getLogger("db")
db_log.debug("Запрос к базе данных выполнен")
```

`network.py`

```python
import logging
import log_config

net_log = logging.getLogger("network")
net_log.warning("Проблема с подключением")
```

---

## Что происходит?

* В `log_config.py` создаём несколько именованных логгеров**, каждый со своей конфигурацией:

  * `"app"` → в консоль + `main.log`
  * `"db"` → только в `db.log`
  * `"network"` → только в `network.log`
* В других файлах создаём логгер с именем нужного варината:

  ```python
  log = logging.getLogger("app")
  ```

  и логируем как обычно.

---

## Плюсы и Минусы подхода

| Плюсы                                   | Минусы                                                         |
|-----------------------------------------| ---------------------------------------------------------------- |
| Просто и понятно — обычный Python-код   | При большом числе логгеров может стать громоздко                 |
| Легко использовать: `import log_config` | Нет гибкой смены настроек (например, через переменные окружения) |
| Каждый логгер пишет в свой файл         | Дублирование форматтера или хендлеров                            |
| Совместимо со старыми версиями Python   | Нет централизованной загрузки из конфигов                        |

