import logging

# Настройка базового логгера
logging.basicConfig(
    level=logging.INFO,                    # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщения
    # можно добавить запись в файл, но при этом потерять вывод в stream:
    filename='simplest.log'
)

if __name__ == "__main__":
    logging.debug("Это сообщение уровня DEBUG (не выведется, т.к. уровень INFO)")
    logging.info("Программа запущена")
    logging.warning("Предупреждение!")
    logging.error("Ошибка!")
    logging.critical("Критическая ошибка!")
