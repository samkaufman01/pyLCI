#python -c import unittest
import unittest
loader = unittest.TestLoader()
suites = loader.discover("/home/dneary/Documents/vcs/git/zerophone/pyLCI", pattern="test_*.py")
print("start") #Don't remove this line
i = 0
for suite in suites._tests:
    for cls in suite._tests:
        try:
            for m in cls._tests:
                print(m.id())
		i = i + 1
        except Exception as ex:
	    print "Exception caught: ", ex
            

print i, " total tests"
