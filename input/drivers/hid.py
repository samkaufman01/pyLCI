from evdev import InputDevice as HID, list_devices, ecodes
from time import sleep
import logging
from skeleton import InputSkeleton

logger = logging.getLogger(__name__)

def get_input_devices():
    """Returns list of all the available InputDevices"""
    return [HID(fn) for fn in list_devices()]

def get_path_by_name(name):
    """Gets HID device path by name, returns None if not found."""
    path = None
    for dev in get_input_devices():
        if dev.name == name:
            path = dev.fn
    return path

def get_name_by_path(path):
    """Gets HID device path by name, returns None if not found."""
    name = None
    for dev in get_input_devices():
        if dev.fn == path:
            name = dev.name
    return name


class InputDevice(InputSkeleton):
    """ A driver for HID devices. As for now, supports keyboards and numpads."""

    def __init__(self, path=None, name=None, **kwargs):
        """Initialises the ``InputDevice`` object.  
                                                                               
        Kwargs:                                                                  
                                                                                 
            * ``path``: path to the input device. If not specified, you need to specify ``name``.
            * ``name``: input device name

        """
        if not name and not path: #No necessary arguments supplied
            raise TypeError("Expected at least path or name; got nothing. =(")
        if not path:
            path = get_path_by_name(name)
            logger.debug("get_path_by_name returned {0} for name {1}".format(path,name))
        if not name:
            name = get_name_by_path(path)
        if not name and not path: #Seems like nothing was found by get_input_devices
            raise IOError("Device not found")
        self.path = path
        self.name = name

        logger.debug("name = {0}, path = {1}".format(name,path))
        self.init_hw()
        InputSkeleton.__init__(self, mapping = [], **kwargs)

    def init_hw(self):
        logger.debug("entered init_hw")
        try:
            logger.debug("attempting to set self.device to self.path={0}".format(self.path))
            self.device = HID(self.path)
        except OSError as osex:
            logger.error("error attempting to set self.device = {0}".format(osex))
            return False
        else:
            logger.debug("grabbing device")
            self.device.grab() #Can throw exception if already grabbed
            logger.debug("device grabbed")
            return True

    def runner(self):
        """Blocking event loop which just calls supplied callbacks in the keymap."""
        logger.debug("entering runner")
        try:
            while not self.stop_flag:
                event = self.device.read_one()
                if event is not None and event.type == ecodes.EV_KEY:
                    key = ecodes.keys[event.code]
                    value = event.value
                    if value == 0 and self.enabled:
                        self.send_key(key)
                sleep(0.01)
        except IOError as e: 
            logger.error("runner IOError = {0}".format(e))
            if e.errno == 11:
                #raise #Uncomment only if you have nothing better to do - error seems to appear at random
                pass

    def atexit(self):
        logger.debug("entered InputDevice.atexit")
        InputSkeleton.atexit(self)
        logger.debug("back from InputSkeleton.atexit")
        try:
            logger.debug("attempting to ungrab hid device")
            self.device.ungrab()
            logger.debug("ungrab successful")
        except Exception as ex:
            logger.error("ungrab failed with ex = {0}".format(ex))
            pass



if __name__ == "__main__":
    print("Available device names:")
    print([dev.name for dev in get_input_devices()])
    #id = InputDevice(name = get_input_devices()[0].name, threaded=False)
    #id.runner()
