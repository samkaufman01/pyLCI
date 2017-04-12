#!/bin/bash
#PATH=$PATH:/home/dneary/Documents/vcs/git/zerophone
#echo $PATH
export PYTHONPATH=/home/dneary/Documents/vcs/git/zerophone
echo $PYTHONPATH
python -m unittest test_path.TestPath
python -m unittest test_manager.TestManager
python -m unittest test_pygame_emulator_factory.TestPyGameEmulator
python -m unittest test_pygame_emulator.TestPyGameEmulator
python -m unittest test_luma_canvas.TestLumaCanvas
python -m unittest test_dialog_box.TestDialogBox
python -m unittest test_menu.TestMenu
python -m unittest test_modem.TestModem

#echo $PATH
