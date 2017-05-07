import PIL
from PIL.ImageOps import invert
from luma.core.render import canvas
from time import sleep
import logging
logger = logging.getLogger(__name__)

def splash(i, o):
    """Displays splash screen"""
    logger.debug("entering splash")
    image = PIL.Image.open("./zerophone/splash.png").convert('L')
    image = invert(image)
    image = image.convert(o.device.mode)
    #note:  the splash screen image size must match the screen size
    #(128 pixels width by 64 pixels height)
    #of the output device or you wil get an exception here.
    #If using the emulator, the exception will be on line 171 of device.py
    #(assert(image.size == self.size))
    o.device.display(image)
    sleep(2)

