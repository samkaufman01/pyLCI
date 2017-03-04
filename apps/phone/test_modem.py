"""test for class Modem (in phone.py)"""

import unittest
import logging
import os
import sys
import modem


#set up logging
LOG_FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestModem(unittest.TestCase):
    """tests Modem class in phone.py"""
    def test_constructor(self):
        """tests constructor"""
        logger.debug("sys.executable = %s", sys.executable)
        logger.debug(
            "entering test_constructor constructor, __package__ is %s, __name__ is %s",
            __package__, __name__)
        logger.debug("os.getcwd()=%s", os.getcwd())
        modem_instance = modem.Modem("/dev/ttyAMA0", timeout=0.2, monitor=True)
        self.assertIsNotNone(modem_instance)

