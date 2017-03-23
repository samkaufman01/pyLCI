
import logging
import unittest
from luma.emulator.device import device

#set up logging
LOG_FORMAT = '%(asctime)-15s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestPyGame(unittest.TestCase):
    def testConstructor(self):
        logger.debug("before invoke")
        game_device = device.pygame()
        self.assertIsNotNone(game_device)
        logger.debug("after unit test")