"""tests manager.py"""
import unittest
#note:  changeing apps.manager to pyLCI.apps.manager breaks vscode test discovery.
#yet pyLint flags the import statement below with W0403, which recommends
#changing the import to pyLCI.apps.manager
#TODO: figure out how to make both vscode and pylint happy
import apps.manager

import logging
from output import output

LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestManager(unittest.TestCase):
    """tests AppManager class"""
    def test_constructor(self):
        """tests AppManager constructor, simplest case"""
        appmanager_instance = apps.manager.AppManager("", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)

    def test_load_skelton_app(self):
        """tests loading skeleton app.
        Currently fails trying to load menu"""
        output.init()
        output_device = output.screen
        appmanager_instance = apps.manager.AppManager("apps", None, None, None, output_device)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("apps/example_apps/skeleton")
        self.assertIsNotNone(app)

    def test_load_clock_app(self):
        """tests loading clock app"""
        appmanager_instance = apps.manager.AppManager("apps", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("apps/clock")
        self.assertIsNotNone(app)

    def test_load_scrolling_test_app(self):
        """tests loading scrolling_test app"""
        output.init()
        output_device = output.screen
        appmanager_instance = apps.manager.AppManager("apps", None, None, None, output_device)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("apps/example_apps/scrolling_test")
        self.assertIsNotNone(app)

def main():
    """tests loading skeleton app"""
    output.init()
    output_device = output.screen
    appmanager_instance = apps.manager.AppManager("apps", None, None, None, output_device)
    app = appmanager_instance.load_app("apps/example_apps/scrolling_test")

if __name__ == "__main__":
    main()
