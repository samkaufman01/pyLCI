from zerophone.helpers import read_config
import importlib
import os
import logging
logger = logging.getLogger(__name__)
screen = None

def init():
    """ This function is called by main.py to
        read the output configuration,
        pick the corresponding drivers
        and initialize a Screen object.

    It also sets ``screen`` global of ``output`` module with created ``Screen`` object."""
    logging.debug("entered output.ini(), os.getcwd()=%s", os.getcwd())
    global screen
    config = read_config("config.json")
    output_config = config["output"][0]
    driver_name = output_config["driver"]
    driver_module = importlib.import_module("zerophone.output.drivers."+driver_name)
    args = output_config["args"] if "args" in output_config else []
    kwargs = output_config["kwargs"] if "kwargs" in output_config else {}
    screen = driver_module.Screen(*args, **kwargs)
