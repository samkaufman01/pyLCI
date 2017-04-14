"""used to troubleshoot vs code python test discovery"""
#python -c import unittest
import unittest
loader = unittest.TestLoader()
suites = loader.discover(start_dir="/home/dneary/Documents/vcs/git/zerophone/tests", 
pattern="test_*.py",
top_level_dir="/home/dneary/Documents/vcs/git/zerophone")
print("start") #Don't remove this line
i = 0
for suite in suites._tests:
    for cls in suite._tests:
        try:
            for m in cls._tests:
                print(m.id())
		i = i + 1
        except Exception as ex:
	    print "Exception caught: {0} in test method {1}".format(ex, cls._testMethodName)
            

print i, " total tests"
