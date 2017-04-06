"""tests manager.py"""
import unittest
import manager
#import pyLCI.apps.example_apps.skeleton
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class TestManager(unittest.TestCase):
    """tests AppManager class"""
    def test_constructor(self):
        """tests AppManager constructor, simplest case"""
        appmanager_instance = manager.AppManager("", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)

    def test_load_skelton_app(self):
        """tests loading skelton app"""
        appmanager_instance = manager.AppManager("apps/", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("skelton")
        self.assertIsNotNone(app)

def main():
    appmanager_instance = manager.AppManager("apps/", None, None, None, None)
    app = appmanager_instance.load_app("skelton")

if __name__ == "__main__":
    main()
