#!/bin/bash
#PATH=$PATH:/home/dneary/Documents/vcs/git/zerophone
#echo $PATH
export PYTHONPATH=/home/dneary/Documents/vcs/git/zerophone
echo $PYTHONPATH
python -m unittest test_path.TestPath
python -m unittest test_manager.TestManager
python -m unittest test_pygame_emulator_factory.TestPyGameEmulator
python -m unittest test_pygame_emulator.TestPyGameEmulator
#echo $PATH
