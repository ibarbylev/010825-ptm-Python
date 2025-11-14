import logging
import sys

# Создаём два хендлера
file_handler = logging.FileHandler("app.log", encoding="utf-8")
console_handler = logging.StreamHandler(sys.stderr)
# console_handler = logging.StreamHandler()  # Можно и без параметров

# Настраиваем формат
formatter = logging.Formatter("%(asctime)s [%(levelname)s] (%(name)s): %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Конфигурация root logger через basicConfig
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[file_handler, console_handler],
    force=True  # очищает старые хендлеры, чтобы не дублировались сообщения
)


if __name__ == "__main__":
    # Проверим
    logging.info("Сообщение INFO — попадёт и в файл, и в консоль")
    logging.error("Сообщение ERROR — тоже в оба места")