"""tests manager.py"""
import unittest
import manager

class TestManager(unittest.TestCase):
    """tests AppManager class"""
    def test_constructor(self):
        """tests AppManager constructor, simplest case"""
        appmanager_instance = manager.AppManager("", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)

    def test_load_skelton_app(self):
        """tests loading skelton app"""
        appmanager_instance = manager.AppManager("", None, None, None, None)
        self.assertIsNotNone(appmanager_instance)
        app = appmanager_instance.load_app("apps/example_apps/skelton")
        self.assertIsNotNone(app)
