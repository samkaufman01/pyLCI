"""test for class DialogBox"""
import unittest
import logging
import os
import sys
#print "os.getcwd()", os.getcwd()
import zerophone.ui.dialog
from zerophone.output import output


#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

class TestDialogBox(unittest.TestCase):
    """tests dialog box class"""
    def test_constructor(self):
        """tests constructor"""
        logger.debug("entering DialogBox test_constructor")
        logger.debug("os.getcwd()=%s", os.getcwd())
        logger.debug('__name__=%s', __name__)
        default_options = "ync"
        output.init("./zerophone/")
        output_device = output.screen
        dialog_box = zerophone.ui.dialog.DialogBox(default_options, None, output_device)
        self.assertIsNotNone(dialog_box)

    def test_keymap(self):
        """tests keymap"""
        logger.debug("entering DialogBox test_constructor")
        logger.debug("os.getcwd()=%s", os.getcwd())
        default_options = "ync"
        output.init("./zerophone/")
        output_device = output.screen
        dialog_box = zerophone.ui.dialog.DialogBox(default_options, None, output_device)
        self.assertIsNotNone(dialog_box.keymap)
        for callback in [dialog_box.keymap[key] for key in dialog_box.keymap.keys()]:
            self.assertIsNotNone(callback)

    def test_dialog_with_real_output(self):
        """tests splicing in real output instead of dummy output"""
        default_options = "ync"
        output.init("./zerophone/")
        output_device = output.screen
        dialog_box = zerophone.ui.dialog.DialogBox(default_options, None, output_device)
        self.assertIsNotNone(dialog_box)

"""
def main():

    sys.path.insert(0, os.getcwd())
    test_suite = unittest.TestLoader().loadTestsFromName("tests.test_dialog_box.TestDialogBox.test_constructor")
    testrunner = unittest.TextTestRunner()
    testrunner.run(test_suite)


if __name__ == "__main__":
    main()
"""