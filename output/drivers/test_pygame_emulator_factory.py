"""tests pygame emulator factory"""

import logging
import unittest
import pygame_emulator_factory

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class TestPyGameEmulator(unittest.TestCase):
    """unit test class for pygame emulator"""
    def test_factory(self):
        """verifies factory returns non-null instance"""
        logger.debug("before invoke")
        emulator_device = pygame_emulator_factory.get_pygame_emulator_device()
        self.assertIsNotNone(emulator_device)
        logger.debug("after unit test")

    def test_factory_set_size(self):
        """tests setting custom size for emulator device window"""
        emulator_device = pygame_emulator_factory.get_pygame_emulator_device(256, 128)
        self.assertIsNotNone(emulator_device)
        logger.debug("after unit test")

"""
used to debug unit test as I can't get the Debug Test function
in VS Code to work (yet)
def main():
    logger.debug("entering main")
    emulator = pygame_emulator_factory.get_pygame_emulator_device()

if __name__ == "__main__":
    main()
"""