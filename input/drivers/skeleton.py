import threading
import logging
logger = logging.getLogger(__name__)

class InputSkeleton():
    """Base class for input devices. Expectations from children:
    
    * ``self.default_mapping`` variable to be set unless you're always going to pass mapping as argument in config
    * ``self.runner`` to be set to a function that'll run in backround, scanning for button presses and sending events to send_key
    * main thread to stop sending keys if self.enabled is False
    * main thread to exit immediately if self.stop_flag is True"""

    enabled = True
    stop_flag = False

    def __init__(self, mapping=None, threaded=True):
        if mapping is not None:
            self.mapping = mapping
        else:
            self.mapping = self.default_mapping
        if threaded:
            self.start_thread()

    def start(self):
        logger.debug("entered start")
        """Sets the ``enabled`` for loop functions to start sending keycodes."""
        self.enabled = True

    def stop(self):
        logger.debug("entered stop")
        """Unsets the ``enabled`` for loop functions to stop sending keycodes."""
        self.enabled = False

    def send_key(self, key):
        logger.debug("entered send_key, key is {0}".format(key))
        """A hook to be overridden by ``InputListener``. Otherwise, prints out key names as soon as they're pressed so is useful for debugging (to test things, just launch the driver as ``python driver.py``)"""
        print(key)

    def start_thread(self):
        """Starts a thread with ``start`` function as target."""
        logger.debug("entered start_thread")
        self.thread = threading.Thread(target=self.runner)
        self.thread.daemon = False
        self.thread.start()
        logger.debug("thread started")
    def atexit(self):
        logger.debug("entered atexit")
        self.stop_flag = True
