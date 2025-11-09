import logging
from persian_logger.logger import get_fa_logger
import unittest


class TestLoggerCore(unittest.TestCase):
    def test_logger_created_once(self):
	    logger1 = get_fa_logger("test_core")
	    logger2 = get_fa_logger("test_core")
	    assert logger1 is logger2

    def test_logger_no_propagation(self):
	    logger = get_fa_logger("core2")
	    assert logger.propagate is False

    def test_logger_has_two_handlers(self):
	    logger = get_fa_logger("core3")
	    assert len(logger.handlers) == 2
