"""test for class DialogBox"""
import unittest
import logging
import os
import zerophone.ui.dialog
import tests.dummyoutputdevice


#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TestDialogBox(unittest.TestCase):
    """tests dialog box class"""
    def test_constructor(self):
        """tests constructor"""
        logger.debug("entering DialogBox test_constructor")
        logger.debug("os.getcwd()=%s", os.getcwd())
        default_options = "ync"
        output_device = tests.dummyoutputdevice.DummyOutputDevice()
        dialog_box = zerophone.ui.dialog.DialogBox(default_options, None, output_device)
        self.assertIsNotNone(dialog_box)

    def test_keymap(self):
        """tests keymap"""
        logger.debug("entering DialogBox test_constructor")
        logger.debug("os.getcwd()=%s", os.getcwd())
        default_options = "ync"
        output_device = tests.dummyoutputdevice.DummyOutputDevice()
        dialog_box = zerophone.ui.dialog.DialogBox(default_options, None, output_device)
        self.assertIsNotNone(dialog_box.keymap)
        for callback in [dialog_box.keymap[key] for key in dialog_box.keymap.keys()]:
            self.assertIsNotNone(callback)