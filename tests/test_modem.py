"""test for class Modem (in phone.py)"""

import unittest
import logging
import os
import sys
import zerophone.apps.phone.modem


#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
_logger = logging.getLogger(__name__)

class TestModem(unittest.TestCase):
    """tests Modem class in phone.py"""
    def test_constructor_no_monitoring(self):
        """tests constructor, with monitoring off (False)"""
        _logger.debug("sys.executable = %s", sys.executable)
        _logger.debug(
            "entering test_constructor constructor, __package__ is %s, __name__ is %s",
            __package__, __name__)
        _logger.debug("os.getcwd()=%s", os.getcwd())
        modem_instance = zerophone.apps.phone.modem.Modem(
            "/dev/ttyAMA0", timeout=0.2, monitor=False)
        self.assertIsNotNone(modem_instance)

'''    def test_constructor_yes_monitoring(self):
        """tests constructor, with monitoring on (True)
           requires mocking serial library
        """
        logger.debug("sys.executable = %s", sys.executable)
        logger.debug(
            "entering test_constructor constructor, __package__ is %s, __name__ is %s",
            __package__, __name__)
        logger.debug("os.getcwd()=%s", os.getcwd())
        #@mock.patch("model.Modem.Serial")
        #TODO: event though this test passes, if you look at the OUTPUT window
        # there is an error in another thread, namely
        #AttributeError: Modem instance has no attribute 'port'
        #this will continue until I get mocking for the serial port figured out
        modem_instance = modem.Modem("/dev/ttyAMA0", timeout=0.2, monitor=True)
        self.assertIsNotNone(modem_instance)'''
