"""tests menu.py"""
import unittest
import logging
import menu
from output import output
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



class TestMenu(unittest.TestCase):
    """tests Menu class"""
    def test_constructor(self):
        """tests constructor"""
        contents = []
        #contents.append("test menu item 1")
        #contents.append(None)
        output.init()
        output_device = output.screen
        menu_instance = menu.Menu(contents, None, output_device, None)
        self.assertIsNotNone(menu_instance)
