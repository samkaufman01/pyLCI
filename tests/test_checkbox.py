'''tests checkbox.py'''
import logging
import unittest
from zerophone.output import output
from zerophone.input import input
import zerophone.ui.checkbox

#set up logging
_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.DEBUG)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)



class TestCheckBox(unittest.TestCase):
    '''tests checkbox control'''
    def test_checkbox_simple_case(self):
        '''tests simplest case, displaying a checkbox and reading returned value'''
        output.init("./zerophone/")
        input.init("./zerophone/")
        i = input.listener
        o = output.screen
        contents = []
        contents.append(["value1", "name1", True])
        contents.append(["value2", "name2", False])
        inp = zerophone.ui.checkbox.Checkbox(contents, i, o)
        self.assertIsNotNone(inp)
        return_data = inp.activate()
        _logger.debug('return_data = %s', return_data)
        inp.deactivate()
        i.atexit()

