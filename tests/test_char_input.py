'''tests char_input'''
import unittest
import logging
import zerophone.ui.char_input
from zerophone.output import output
from zerophone.input import input

#set up logging
_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.INFO)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)

class TestCharInput(unittest.TestCase):
    '''tests char_input control'''
    def test_char_input_simple(self):
        '''tests simple case of just displaying text and hitting enter
           to validate correct value is returned'''
        output.init("./zerophone/")
        input.init("./zerophone/")
        i = input.listener
        o = output.screen
        inp = zerophone.ui.char_input.CharArrowKeysInput(i, o, "Hey")
        self.assertIsNotNone(inp)
        selected_value = inp.activate()
        self.assertEqual("Hey", selected_value)
        inp.deactivate()
        i.atexit()

