import logging
import io
from persian_logger.formatter import FilePersianFormatter
import unittest

class TestFileFormatter(unittest.TestCase):
    def test_file_formatter_basic(self):
        stream = io.StringIO()
        h = logging.StreamHandler(stream)
        h.setFormatter(FilePersianFormatter())

        logger = logging.getLogger("filetest")
        logger.handlers.clear()
        logger.setLevel(logging.INFO)
        logger.addHandler(h)

        logger.info("سلام فایل")
        out = stream.getvalue()

        assert "ﻡﻼﺳ" in out
        assert "|" in out
