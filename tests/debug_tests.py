import unittest
import logging
import sys
import os

#set up logging
LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)

def debug_all_tests():
    suites = unittest.defaultTestLoader.discover(
        start_dir="/home/dneary/Documents/vcs/git/zerophone/tests",
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
    """allows debugging a single test class"""
    test_class_to_debug = "TestLumaCanvas"
    top_level_dir = "/home/dneary/Documents/vcs/git/zerophone"

    suites = unittest.defaultTestLoader.discover(
        "/home/dneary/Documents/vcs/git/zerophone/tests",
        pattern='test_*.py',
        top_level_dir=top_level_dir)

    assert top_level_dir in sys.path

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

def debug_without_discover():
    """simplified test debugging without having to use the opaque test discovery tool"""
    start_dir = "/home/dneary/Documents/vcs/git/zerophone/tests"
    top_level_dir = "/home/dneary/Documents/vcs/git/zerophone"

    #test_class_to_debug = "tests.TestDialogBox"
    module_name = "test_dialog_box"
    #this assumes your tests are separate from your source code
    #and your tests are stored in a folder name tests
    dotted_module_name = "tests." + module_name
    python_file_name = module_name + ".py"
    python_file_location = os.path.join(start_dir, python_file_name)

    test_method_name_prefix = "test_"

    #verify paths and files are located where I think they are.
    #package and module loading are very sensitive to these paths
    assert top_level_dir not in sys.path
    sys.path.insert(0, top_level_dir)
    assert top_level_dir in sys.path
    assert top_level_dir == os.getcwd()
    assert os.path.exists(python_file_location)

    logger.debug("importing dotted_module_name %s", dotted_module_name)
    import_module = __import__(dotted_module_name)

    import inspect
    #import imp
    #(getmoduleinfo_name, getmoduleinfo_suffix, getmoduleinfo_mode, getmoduleinfo_module_type) = \
    #inspect.getmoduleinfo(full_path)
    #logger.debug('imp.PY_SOURCE=%s', imp.PY_SOURCE)
    #assert getmoduleinfo_module_type == imp.PY_SOURCE
    test_methods = []
    members = inspect.getmembers(import_module)
    for member in members:
        logger.debug('type(member)=%s, member=%s', type(member), member)
        (member_name, member_value) = member
        logger.debug('member_name=%s, member_value=%s', member_name, member_value)
        if member_name == module_name:
            member_classes = inspect.getmembers(member_value, inspect.isclass)
            logger.debug('member_class count =%d', len(member_classes))
            #assume (and assert) only 1 test class per module
            assert len(member_classes) == 1
            first_member_class_item = member_classes[0]
            (first_member_class_name, first_member_class_value) = first_member_class_item
            is_unit_test_sub_class = issubclass(first_member_class_value, unittest.TestCase)
            logger.debug('first_member_class_name %s is_unit_test_sub_class=%r',
                         first_member_class_name, is_unit_test_sub_class)
            if is_unit_test_sub_class:
                method_list = dir(first_member_class_value)
                logger.debug('method_list=%s', method_list)
                for method in method_list:
                    logger.debug("examining method %s", method)
                    if isTestMethod(method, first_member_class_value, test_method_name_prefix):
                        logger.debug('method %s is a test method', method)
                        test_methods.append(method)

    logger.debug('test_methods=%s', test_methods)

def isTestMethod(attrname, testCaseClass, test_method_name_prefix):
    """returns true if attrname is a test method, false otherwise"""

    logger.debug('attrname=%s', attrname)
    logger.debug('test_method_name_prefix=%s', test_method_name_prefix)
    logger.debug('attrname.startswith(preftest_method_name_prefixix)=%s',
                 attrname.startswith(test_method_name_prefix))
    logger.debug('getattr(testCaseClass, attrname)=%s',
                 getattr(testCaseClass, attrname))
    logger.debug('hasattr(getattr(testCaseClass, attrname), "__call__")=%r',
                 hasattr(getattr(testCaseClass, attrname), '__call__'))
    function_return = attrname.startswith(test_method_name_prefix) and \
    hasattr(getattr(testCaseClass, attrname), '__call__')

    logger.debug('function_return=%r', function_return)
    return function_return


if __name__ == "__main__":
    #debug_one_test_class()
    #debug_all_tests()
    debug_without_discover()

