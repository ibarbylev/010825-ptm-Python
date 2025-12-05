import logging
import log_config  # ← подключает все логгеры

log = logging.getLogger("app")
log.info("Привет из основного модуля")