import os
import logging
import io
from unittest.mock import patch
from persian_logger.formatter import ConsolePersianFormatter
import unittest

class TestRtlTerminal(unittest.TestCase):
    def get_test_logger(self):
        stream = io.StringIO()
        h = logging.StreamHandler(stream)
        h.setFormatter(ConsolePersianFormatter())
        logger = logging.getLogger("rtl_test")
        logger.handlers.clear()
        logger.setLevel(logging.INFO)
        logger.addHandler(h)
        return logger, stream

    def test_rtl_disabled_ubuntu(self):
        with patch.dict(os.environ, {"TERM_PROGRAM": ""}):
            logger, stream = self.get_test_logger()
            logger.info("این DEBUG است")
            out = stream.getvalue()
            assert "DEBUG" in out
            idx_est  = out.index("ﺍﺳﺖ")
            idx_debug = out.index("DEBUG")
            idx_ein  = out.index("ﺍﯾﻦ")
            assert idx_est < idx_debug < idx_ein

    def test_rtl_enabled_vscode(self):
        with patch.dict(os.environ, {"TERM_PROGRAM": "vscode"}):
            logger, stream = self.get_test_logger()
            logger.info("این DEBUG است")
            out = stream.getvalue()

            assert "DEBUG" in out
            assert "ﻦﯾﺍ" in out
            assert "ﺖﺳﺍ" in out  
