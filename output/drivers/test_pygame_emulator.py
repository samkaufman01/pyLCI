
import logging
import unittest
import demo_arg_parser

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TestPyGame(unittest.TestCase):
    def testConstructor(self):
        logger.debug("before invoke")
        game_device = demo_arg_parser.get_device()
        self.assertIsNotNone(game_device)
        logger.debug("after unit test")
