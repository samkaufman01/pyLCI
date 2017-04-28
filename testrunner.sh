#!/bin/bash
python -m unittest discover -s /home/dneary/Documents/vcs/git/zerophone/tests/ -p "test_*.py" -t /home/dneary/Documents/vcs/git/zerophone
#unfortunately I can't use this (better) syntax - discovery throws error
#File "/usr/lib/python2.7/unittest/loader.py", line 226, in _get_name_from_path
#    assert not _relpath.startswith('..'), "Path must be within the project"
#this is a bug
#TODO: file a bug report
#python -m unittest discover -s ./tests/ -p "test_*.py" -t ./zerophone/