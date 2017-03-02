"""test for class DialogBox"""

import unittest
import logging
import phone

#set up logging
LOG_FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestModem(unittest.TestCase):
    """tests Modem class in phone.py"""
    def test_constructor(self):
        """tests constructor"""
        modem_instance = phone.Modem("/dev/ttyAMA0", timeout=0.2, monitor=False)
        self.assertIsNotNone(modem_instance)

