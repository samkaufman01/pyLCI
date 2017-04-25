"""tests menu.py"""
import unittest
import logging
import os
import zerophone.ui.menu
from zerophone.output import output
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

class TestMenu(unittest.TestCase):
    """tests Menu class"""
    def test_constructor(self):
        """tests constructor"""
        logger.debug("os.getcwd()=%s", os.getcwd())
        contents = []
        output.init("./zerophone/")
        output_device = output.screen
        menu_instance = zerophone.ui.menu.Menu(contents, None, output_device, None)
        self.assertIsNotNone(menu_instance)

"""
def main():
    contents = []
    output.init("./zerophone/")
    output_device = output.screen
    menu_instance = zerophone.ui.menu.Menu(contents, None, output_device, None)

if __name__ == "main":
    main()
"""
