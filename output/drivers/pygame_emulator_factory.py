"""
transition shim code, this is in the process of being refactored away
"""
import logging
import luma.emulator.device

# ignore PIL debug messages
logging.getLogger("PIL").setLevel(logging.ERROR)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_pygame_emulator_device():
    """
    hard wired to return pygame emulator device
    """

    #these are the bare minimum attributes needed to construct the emulator
    emulator_attributes = {}
    emulator_attributes['display'] = 'pygame'
    emulator_attributes['height'] = 64
    emulator_attributes['rotate'] = 0
    emulator_attributes['scale'] = 2
    emulator_attributes['transform'] = 'scale2x'
    emulator_attributes['width'] = 128


    Device = getattr(luma.emulator.device, 'pygame')

    device = Device(**emulator_attributes)

    return device
