"""tests menu.py"""
import unittest
import menu

class TestMenu(unittest.TestCase):
    """tests Menu class"""
    def test_constructor(self):
        """tests constructor"""
        contents = []
        contents.append("test menu item 1")
        contents.append(None)
        menu_instance = menu.Menu(contents, None, None, None)
        self.assertIsNotNone(menu_instance)
