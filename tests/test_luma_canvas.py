"""tests luma canvas drawing capabilities"""

import logging
import unittest
from luma.core.render import canvas
import zerophone.output.drivers.pygame_emulator_factory

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

#pygame_emulator_factory sets width to 128 pixels and height to 64 pixels
#set it to a different value here to make sure there are no hard coded
#assumptions buried in the zerophone code.
EMULATOR_WINDOW_WIDTH = 256
EMULATOR_WINDOW_HEIGHT = 128

class TestLumaCanvas(unittest.TestCase):
    """unit test class to verify luma emulator canvas object functionality"""
    def test_canvas_draw_rectangle(self):
        """verifies capabilities of pygame emulator draw rectangle method"""
        device = zerophone.output.drivers.pygame_emulator_factory.get_pygame_emulator_device(
            EMULATOR_WINDOW_WIDTH,
            EMULATOR_WINDOW_HEIGHT)

        with canvas(device) as draw:
            #box_boundary is in pixels, upper left, lower right
            box_boundary = (0, 0, 128, 128)
            logger.debug("box_boundary: %s", box_boundary)
            draw.rectangle(box_boundary, outline="blue")

    def test_canvas_draw_text(self):
        """tests printing text to the emulator.
            Expected Result: 2 lines of text drawn in different places.
            Actual Result:  2 lines of text drawn in different places
            """
        device = zerophone.output.drivers.pygame_emulator_factory.get_pygame_emulator_device(
            EMULATOR_WINDOW_WIDTH,
            EMULATOR_WINDOW_HEIGHT)

        with canvas(device) as draw:
            #x,y are in pixels
            text_start_x_y = (64, 64)
            draw.text(text_start_x_y, "hello world 64,64", fill="blue")
            #this should draw above the other text, it is a test of
            #if the text is erased by subsequent calls (it is not)
            text_start_x_y = (32, 32)
            draw.text(text_start_x_y, "hello world 32,32", fill="red")

    def test_canvas_draw_combined(self):
        """tests drawing text with a bounding rectangle.
           Expected result:  2 lines of text with a rectangle bounding the entire emulator window.
           Actual result: 2 lines of text with a rectangle bounding the entire emulator window.
        """
        device = zerophone.output.drivers.pygame_emulator_factory.get_pygame_emulator_device(
            EMULATOR_WINDOW_WIDTH,
            EMULATOR_WINDOW_HEIGHT)

        with canvas(device) as draw:
            #x,y are in pixels
            text_start_x_y = (64, 64)
            draw.text(text_start_x_y, "hello world 64,64", fill="blue")
            #this should draw above the other text, it is a test of
            #if the text is erased by subsequent calls (it is not)
            text_start_x_y = (32, 32)
            draw.text(text_start_x_y, "hello world 32,32", fill="red")
            box_boundary = (0, 0, EMULATOR_WINDOW_WIDTH - 1, EMULATOR_WINDOW_HEIGHT - 1)
            draw.rectangle(box_boundary, outline="yellow")


"""
used to debug unit test as I can't get the Debug Test function
in VS Code to work (yet)
def main():
    device = pygame_emulator_factory.get_pygame_emulator_device(EMULATOR_WINDOW_WIDTH,
                                                                EMULATOR_WINDOW_HEIGHT)

    with canvas(device) as draw:
        #x,y are in pixels
        text_start_x_y = (64, 64)
        draw.text(text_start_x_y, "hello world 64,64", fill="blue")
        #this should draw above the other text, it is a test of
        #if the text is erased by subsequent calls (it is not)
        text_start_x_y = (32, 32)
        draw.text(text_start_x_y, "hello world 32,32", fill="red")
        box_boundary = (0, 0, EMULATOR_WINDOW_WIDTH - 1, EMULATOR_WINDOW_HEIGHT - 1)
        draw.rectangle(box_boundary, outline="yellow")

if __name__ == "__main__":
    main()
"""