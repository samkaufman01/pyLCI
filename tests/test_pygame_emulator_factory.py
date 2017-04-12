"""tests pygame emulator factory"""

import logging
import unittest

import sys
#sys.path.append('/home/dneary/Documents/vcs/git/zerophone')
import os
#os.chdir('/home/dneary/Documents/vcs/git/zerophone/zerophone')

import zerophone.output.drivers.pygame_emulator_factory

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)


class TestPyGameEmulator(unittest.TestCase):
    """unit test class for pygame emulator"""
    def test_factory(self):
        """verifies factory returns non-null instance"""
        logger.debug("before invoke")
        emulator_device = zerophone.output.drivers.pygame_emulator_factory.get_pygame_emulator_device()
        self.assertIsNotNone(emulator_device)
        logger.debug("after unit test")

    def test_factory_set_size(self):
        """tests setting custom size for emulator device window"""
        emulator_device = zerophone.output.drivers.pygame_emulator_factory.get_pygame_emulator_device(256, 128)
        self.assertIsNotNone(emulator_device)
        logger.debug("after unit test")

"""
used to debug unit test as I can't get the Debug Test function
in VS Code to work (yet)
"""
def main():
    logger.debug("entering main")
    emulator = zerophone.output.drivers.pygame_emulator_factory.get_pygame_emulator_device()

if __name__ == "__main__":
    main()

