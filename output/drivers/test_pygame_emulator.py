"""tests pygame emulator"""

import logging
import unittest
import pygame_emulator_factory



#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class TestPyGame(unittest.TestCase):
    """unit test class for pygame emulator"""
    def test_constructor(self):
        """tests constructor"""
        logger.debug("before invoke")
        emulator = pygame_emulator_factory.get_pygame_emulator_device()
        self.assertIsNotNone(emulator)
        logger.debug("after unit test")


def main():
    logger.debug("entering main")
    emulator = pygame_emulator_factory.get_pygame_emulator_device()

if __name__ == "__main__":
    main()
