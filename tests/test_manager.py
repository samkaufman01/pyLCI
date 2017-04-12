"""tests manager.py"""
import sys

import unittest
#note:  changing apps.manager to zerophone.apps.manager breaks vscode test discovery.
#yet pyLint flags the import statement below with W0403, which recommends
#changing the import to zerophone.apps.manager
#TODO: figure out how to make both vscode and pylint happy
import zerophone.apps.manager

import logging
from zerophone.output import output

LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug("sys.path=%s", sys.path)

class TestManager(unittest.TestCase):
    """tests AppManager class"""
    def test_constructor(self):
        """tests AppManager constructor, simplest case"""
        appmanager_instance = zerophone.apps.manager.AppManager("", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)

    def test_load_skelton_app(self):
        """tests loading skeleton app.
        """
        output.init("../zerophone/")
        output_device = output.screen
        appmanager_instance = zerophone.apps.manager.AppManager("apps", None, None, None, output_device)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("zerophone/apps/example_apps/skeleton")
        self.assertIsNotNone(app)

    def test_load_clock_app(self):
        """tests loading clock app"""
        appmanager_instance = zerophone.apps.manager.AppManager("apps", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("zerophone/apps/clock")
        self.assertIsNotNone(app)

    def test_load_scrolling_test_app(self):
        """tests loading scrolling_test app"""
        output.init("../zerophone/")
        output_device = output.screen
        appmanager_instance = zerophone.apps.manager.AppManager("apps", None, None, None, output_device)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("zerophone/apps/example_apps/scrolling_test")
        self.assertIsNotNone(app)

"""
#Workaround for Debug Test not yet working in vscode
def main():
    output.init()
    output_device = output.screen
    appmanager_instance = zerophone.apps.manager.AppManager("apps", None, None, None, output_device)
    #self.assertIsNotNone(appmanager_instance)
    app = appmanager_instance.load_app("zerophone/apps/example_apps/skeleton")
    #self.assertIsNotNone(app)

if __name__ == "__main__":
    main()
"""
