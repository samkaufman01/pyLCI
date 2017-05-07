import importlib
import os
import logging
from zerophone.helpers.config_parse import read_config
logger = logging.getLogger(__name__)
screen = None

def init(path_to_config_json=None):
    """ This function is called by main.py to
        read the output configuration,
        pick the corresponding drivers
        and initialize a Screen object.

    It also sets ``screen`` global of ``output`` module with created ``Screen`` object."""
    logger.debug("entered output.init(), os.getcwd()=%s", os.getcwd())
    global screen

    config_file = "config.json"
    if path_to_config_json is not None:
        config_file = path_to_config_json + config_file
    config = read_config(config_file)
    output_config = config["output"][0]
    driver_name = output_config["driver"]
    driver_module = importlib.import_module("zerophone.output.drivers."+driver_name)
    args = output_config["args"] if "args" in output_config else []
    kwargs = output_config["kwargs"] if "kwargs" in output_config else {}
    screen = driver_module.Screen(*args, **kwargs)
