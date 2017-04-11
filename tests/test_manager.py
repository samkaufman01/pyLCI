"""tests manager.py"""
import sys
sys.path.append('/home/dneary/Documents/vcs/git/zerophone')
import os
os.chdir('/home/dneary/Documents/vcs/git/zerophone/pyLCI')

import unittest
#note:  changing apps.manager to pyLCI.apps.manager breaks vscode test discovery.
#yet pyLint flags the import statement below with W0403, which recommends
#changing the import to pyLCI.apps.manager
#TODO: figure out how to make both vscode and pylint happy
import pyLCI.apps.manager

import logging
from pyLCI.output import output

LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestManager(unittest.TestCase):
    """tests AppManager class"""
    def test_constructor(self):
        """tests AppManager constructor, simplest case"""
        appmanager_instance = pyLCI.apps.manager.AppManager("", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)

    def test_load_skelton_app(self):
        """tests loading skeleton app.
        """
        output.init()
        output_device = output.screen
        appmanager_instance = pyLCI.apps.manager.AppManager("apps", None, None, None, output_device)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("apps/example_apps/skeleton")
        self.assertIsNotNone(app)

    def test_load_clock_app(self):
        """tests loading clock app"""
        appmanager_instance = pyLCI.apps.manager.AppManager("apps", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("apps/clock")
        self.assertIsNotNone(app)

    def test_load_scrolling_test_app(self):
        """tests loading scrolling_test app"""
        output.init()
        output_device = output.screen
        appmanager_instance = pyLCI.apps.manager.AppManager("apps", None, None, None, output_device)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("apps/example_apps/scrolling_test")
        self.assertIsNotNone(app)


#Workaround for Debug Test not yet working in vscode
def main():
    output.init()
    output_device = output.screen
    appmanager_instance = pyLCI.apps.manager.AppManager("apps", None, None, None, output_device)
    #self.assertIsNotNone(appmanager_instance)
    app = appmanager_instance.load_app("pyLCI/apps/example_apps/skeleton")
    #self.assertIsNotNone(app)

if __name__ == "__main__":
    main()

