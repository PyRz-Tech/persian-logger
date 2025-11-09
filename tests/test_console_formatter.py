import logging
import io
import unittest
from persian_logger.formatter import ConsolePersianFormatter


class DummyHandler(logging.Handler):
	def __init__(self):
		super().__init__()
		self.buffer = ""


	def emit(self, record):
		msg = self.format(record)
		self.buffer += msg



class TestConsole(unittest.TestCase):

    def setUp(self):
        self.handler = DummyHandler()
        
    def make_logger(self, formatter):
	    logger = logging.getLogger("console_test")
	    logger.setLevel(logging.DEBUG)
	    logger.handlers.clear()

	    handler = self.handler
	    handler.setFormatter(formatter)
	    logger.addHandler(handler)

	    return logger, handler


    def test_console_simple_fa(self):
	    logger, h = self.make_logger(ConsolePersianFormatter())
	    logger.info("سلام helloجهانم ")
	    assert "hello" in h.buffer

    def test_console_no_duplicate(self):
        logger, h = self.make_logger(ConsolePersianFormatter())
        logger.info("تست")
        logger.info("تست")
        out = h.buffer
        assert out.count("(") == 2
        assert out.count(")") == 2
        assert "ﺗﺴﺖ" in out 
