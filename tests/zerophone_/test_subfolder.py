"""test of subfolders"""
import unittest
import logging
import zerophone.ui.dialog
from zerophone.output import output

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
_logger = logging.getLogger(__name__)

class TestSubFolder(unittest.TestCase):
    def test_hello(self):
        _logger.debug("hello world")

    def test_zerophone_import(self):
        """tests importing code from a subfolder"""
        default_options = "ync"
        output.init("./zerophone/")
        output_device = output.screen
        dialog_box = zerophone.ui.dialog.DialogBox(default_options, None, output_device)
        self.assertIsNotNone(dialog_box)
