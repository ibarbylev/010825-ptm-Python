import logging
import log_config

db_log = logging.getLogger("db")
db_log.debug("Запрос к базе данных выполнен")