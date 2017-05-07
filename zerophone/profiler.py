import cProfile
import sys
sys.path.insert(0,"/home/dneary/Documents/vcs/git/zerophone")
import zerophone
cProfile.run("zerophone.main()")