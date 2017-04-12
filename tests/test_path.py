"""experimental path tinkering"""

import logging
import sys
import unittest
import os

LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug("in module sys.path=%s", sys.path)

class TestPath(unittest.TestCase):
    """tests injecting path via bash scripts"""
    def test_path(self):
        """tests adding path via bash in testrunner.sh, simplest case"""
        #logger.debug("value of PYTHONPATH is %s", os.environ['PYTHONPATH'])
        logger.debug("in test case test_path.  sys.path=%s", sys.path)
        self.assertIn('/home/dneary/Documents/vcs/git/zerophone', sys.path)
