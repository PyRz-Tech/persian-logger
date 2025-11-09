import logging
from persian_logger.converter import PersianConverter
from persian_logger.terminal_supports_rtl import TerminalSupport

class BasePersianFormatter(logging.Formatter):

    _LEVEL_MAP = {
        'DEBUG': 'اشکال‌زدایی',
        'INFO': 'اطلاعات',
        'WARNING': 'هشدار',
        'ERROR': 'خطا',
        'CRITICAL': 'بحرانی'
    }

    def __init__(self, fmt=None, datefmt=None):
        default_fmt = fmt or "%(asctime)s | %(levelname)s | %(message)s"
        super().__init__(fmt or default_fmt, datefmt)
        self.persian_numbers = True

    def formatTime(self, record, datefmt):
        if self.persian_numbers:
            return PersianConverter.now_persian()
        return super().formatTime(record, datefmt)

    def _smart_convert(self, text):
        return PersianConverter.full_convert(text)

    def format(self, record):
        record.msg = self._smart_convert(record.msg)
        record.levelname = self._smart_convert(
            self._LEVEL_MAP.get(record.levelname, record.levelname)
        )
        return super().format(record)

class FilePersianFormatter(BasePersianFormatter):
    pass

class ConsolePersianFormatter(BasePersianFormatter):
    def __init__(self):
        fmt = "[ %(asctime)s | %(levelname)s ] ( %(message)s )"
        super().__init__(fmt=fmt)

    def format(self, record):
        if TerminalSupport.terminal_supports_rtl():
            return super().format(record)
            
        msg = record.getMessage()
        msg = PersianConverter._pseudo_rtl(msg)
        record.msg = self._smart_convert(msg)
        record.levelname = self._smart_convert(
            self._LEVEL_MAP.get(record.levelname, record.levelname)
        )
        return super().format(record)

