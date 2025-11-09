import logging
from logging.handlers import RotatingFileHandler
import sys
from persian_logger.formatter import FilePersianFormatter, ConsolePersianFormatter

def get_fa_logger(
    name: str = "FarsiApp",
    log_file: str = "app.log",
    level = logging.DEBUG,
    persian_numbers: bool = True,
    max_bytes: int = 1_000_000,
    backup_count: int = 3
) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if logger.handlers:
        logger.handlers.clear()

    formatter_file = FilePersianFormatter()
    formatter_consule = ConsolePersianFormatter()
    
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter_file)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter_consule)
    logger.addHandler(console_handler)

    return logger
