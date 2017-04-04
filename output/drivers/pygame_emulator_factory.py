"""
factory for pygame emulator device
sets minimum attributes,
creates device
returns it to caller
"""
import logging
import luma.emulator.device

# ignore PIL debug messages
logging.getLogger("PIL").setLevel(logging.ERROR)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_pygame_emulator_device(width=128, height=64):
    """
    creates and returns pygame emulator device
    """

    #these are the bare minimum attributes needed to construct the emulator
    emulator_attributes = {}
    emulator_attributes['display'] = 'pygame'
    #width and height are in pixels
    emulator_attributes['width'] = width
    emulator_attributes['height'] = height

    Device = getattr(luma.emulator.device, 'pygame')

    device = Device(**emulator_attributes)

    return device
