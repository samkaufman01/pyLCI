#!/bin/bash
#uses test discovery to recursively run all unit tests in pyLCI 
python -m unittest discover -s "/home/dneary/Documents/vcs/git/zerophone/pyLCI" -p "test_*.py" 

