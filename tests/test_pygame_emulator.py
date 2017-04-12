"""tests pygame emulator
    Crude at the moment as the expected result
    must be visually observed.
    TODO: fix this.
"""

import logging
import unittest

import zerophone.output.drivers.pygame_emulator

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.ERROR)
logger = logging.getLogger(__name__)


class TestPyGameEmulator(unittest.TestCase):
    """tests pygame emulator public methods"""
    def test_screen_display_hello_world(self):
        """ simple test of displaying hello world
            Expected result:  a window will flash on the screen with "hello world" then
            the window will disappear as screen goes out of scope
        """
        screen = zerophone.output.drivers.pygame_emulator.Screen()
        #should flash a window on the screen with hello world
        screen.display_data("hello world")

    def test_set_cursor(self):
        """ tests displaying text at various positions on the screen
            Expected result:  a window will flash on the screen with "row 4, column 5" then
            the window will disappear as screen goes out of scope
            Actual result:  text is always displayed at row 1, column 1
        """
        screen = zerophone.output.drivers.pygame_emulator.Screen()
        screen.setCursor(4, 5)
        screen.display_data("row 4, column 5")

    def test_display_text_list(self):
        """ tests displaying 2 lines of text passed in as a list.
            Expected result:  2 lines of text displayed on screen
            Actual result: exception thrown out of PIL/ImageDraw.py
        """
        screen = zerophone.output.drivers.pygame_emulator.Screen()
        screen_data = ['row 1', 'row 2']
        #TODO:  SystemError is an internal exception in the python
        #interpreter and should eventually be reported to the python
        #maintainer
        with self.assertRaises(SystemError):
            screen.display_data(screen_data)
    def test_display_text_tuple(self):
        """ tests displaying 3 lines of text passed in as a tuple.
            Expected result:  3 lines of text displayed on screen
            Actual result: exception thrown out of PIL/ImageDraw.py
            SystemError, error return without exception set
        """
        screen = zerophone.output.drivers.pygame_emulator.Screen()
         #note:  when passing data via *args like display_data does,
        #python silently creates a tuple out of these args.
        #so screen_data becomes a tuple inside a second tuple,
        #which causes an exception
        screen_data = ('row 1', 'row 2', 'row 3')
        #TODO:  SystemError is an internal exception in the python
        #interpreter and should eventually be reported to the python
        #maintainer
        with self.assertRaises(SystemError):
            screen.display_data(screen_data)

    def test_display_text_multiple_args(self):
        """ tests displaying 3 lines of text passed in as a tuple.
            Expected result:  3 lines of text displayed on screen
            Actual result: 3 lines of text displayed on screen
        """
        screen = zerophone.output.drivers.pygame_emulator.Screen()
        #note:  when passing data via *args like display_data does,
        #python silently creates a tuple out of these args
        screen.display_data('row 1', 'row 2', 'row 3')

    def test_display_multiline_text(self):
        """tests displaying 3 lines of text separated by line feeds
           Expected result:  3 lines of text are shown on screen.
           Actual result:  3 lines of text are shown on screen."""
        screen = zerophone.output.drivers.pygame_emulator.Screen()
        screen_data = '\n'.join(['row 1', 'row 2', 'row 3'])
        screen.display_data(screen_data)

"""
used to debug unit test as I can't get the Debug Test function
in VS Code to work (yet)
"""
def main():
    logging.basicConfig(format=LOG_FORMAT)
    #logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    screen = zerophone.output.drivers.pygame_emulator.Screen()
    #note:  when passing data via *args like display_data does,
    #python silently creates a tuple out of these args
    screen.display_data('row 1', 'row 2', 'row 3')

if __name__ == "__main__":
    main()
