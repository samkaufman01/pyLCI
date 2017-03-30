"""test for class DialogBox"""

import unittest
import logging
import os
import dialog
import dummyoutputdevice


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
        output_device = dummyoutputdevice.DummyOutputDevice()
        dialog_box = dialog.DialogBox(default_options, None, output_device)
        self.assertIsNotNone(dialog_box)
