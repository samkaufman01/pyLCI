import unittest
import logging
#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def debug_all_tests():
    suites = unittest.defaultTestLoader.discover(
        "/home/dneary/Documents/vcs/git/zerophone/tests",
        pattern='test_*.py',
        top_level_dir="/home/dneary/Documents/vcs/git/zerophone")

    testrunner = unittest.TextTestRunner()
    #testrunner.run(testsuite)
    #logger.debug("found %d suites", len(suites))
    for suite in suites:
        #logger.debug("%d tests in suite %s", len(suite._tests[0]._tests), suite._tests[0]._tests)
        test_class_name = type(suite._tests[0]._tests[0]).__name__
        logger.debug("Test Class %s has %d tests", test_class_name , len(suite._tests[0]._tests))
        for testcase in suite._tests[0]._tests:
            logger.debug("test method %s", testcase._testMethodName)
        #testrunner.run(suite)

def debug_one_test_class():

    
    test_class_to_debug = "TestLumaCanvas"

    suites = unittest.defaultTestLoader.discover(
        "/home/dneary/Documents/vcs/git/zerophone/tests",
        pattern='test_*.py',
        top_level_dir="/home/dneary/Documents/vcs/git/zerophone")

    testrunner = unittest.TextTestRunner()
    for suite in suites:
        #logger.debug("%d tests in suite %s", len(suite._tests[0]._tests), suite._tests[0]._tests)
        test_class_name = type(suite._tests[0]._tests[0]).__name__
        #logger.debug("Test Class %s has %d tests", test_class_name , len(suite._tests[0]._tests))
        #for testcase in suite._tests[0]._tests:
        #    logger.debug("test method %s", testcase._testMethodName)
        if test_class_name == test_class_to_debug:
            logger.debug("matched test class %s, running suite", test_class_name)
            testrunner.run(suite)

if __name__ == "__main__":
    debug_one_test_class()
    #debug_all_tests()
    
