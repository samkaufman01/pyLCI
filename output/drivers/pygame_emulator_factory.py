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

def get_pygame_emulator_device():
    """
    creates and returns pygame emulator device
    """

    #these are the bare minimum attributes needed to construct the emulator
    emulator_attributes = {}
    emulator_attributes['display'] = 'pygame'
    emulator_attributes['width'] = 256
    emulator_attributes['height'] = 64
    emulator_attributes['rotate'] = 0
    emulator_attributes['scale'] = 2
    emulator_attributes['transform'] = 'scale2x'


    Device = getattr(luma.emulator.device, 'pygame')

    device = Device(**emulator_attributes)

    return device
