'''test for unittest'''

import unittest
#set up logging
import logging
_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.INFO)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)

class TestUnitTesting(unittest.TestCase):
    '''test class'''
    def test_constructor(self):
        '''tests constructor'''
        foo2 = "foo"
        self.assertTrue(foo2 == "foo")
