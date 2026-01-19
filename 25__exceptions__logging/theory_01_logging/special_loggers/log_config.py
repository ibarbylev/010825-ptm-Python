import logging
import sys

# --- Общий формат ---
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] (%(name)s): %(message)s"
)

# --- Конфиг для основного приложения ("app") ---
file_handler_main = logging.FileHandler("main.log", encoding="utf-8")
file_handler_main.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stderr)
# console_handler = logging.StreamHandler()  # Можно и без параметров
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