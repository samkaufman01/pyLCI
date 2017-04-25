"""tests pygame emulator factory"""

import logging
import unittest
import sys
import os
import zerophone.output.drivers.pygame_emulator_factory

#print "sys.argv", sys.argv
#print "os.getcwd()", os.getcwd()

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)


class TestPyGameEmulator(unittest.TestCase):
    """unit test class for pygame emulator"""
    def test_factory(self):
        """verifies factory returns non-null instance"""
        #print "sys.argv", sys.argv
        #print "os.getcwd()", os.getcwd()
        logger.debug("before invoke")
        #adding an __init__.py to /home/dneary/Documents/vcs/git/zerophone
        #will cause this import to fail
        emulator_device = zerophone.output.drivers.pygame_emulator_factory.\
        get_pygame_emulator_device()
        self.assertIsNotNone(emulator_device)
        logger.debug("after unit test")

    def test_factory_set_size(self):
        """tests setting custom size for emulator device window"""
        #print "sys.argv", sys.argv
        #print "os.getcwd()", os.getcwd()
        emulator_device = zerophone.output.drivers.pygame_emulator_factory.\
        get_pygame_emulator_device(256, 128)
        self.assertIsNotNone(emulator_device)
        logger.debug("after unit test")


