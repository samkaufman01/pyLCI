menu_name = "File browser" 

from ui import PathPicker, Printer
import os
import string

#Callback global for pyLCI. It gets called when application is activated in the main menu
callback = None

#Some globals for us
i = None #Input device
o = None #Output device

def init_app(input, output):
    global callback, i, o
    i = input; o = output #Getting references to output and input device objects and saving them as globals
    callback = browse

def print_path(path):
    if os.path.isdir(path):
        Printer("Dir: {}".format(path), i, o, 5)
    elif os.path.isfile(path):
        Printer("File: {}".format(path), i, o, 5)
    else:
        Printer("WTF: {}".format(path), i, o, 5) # ;-P

def is_text(filename):
    s=open(filename).read(512)
    text_characters = "".join(map(chr, range(32, 127)) + list("\n\r\t\b"))
    _null_trans = string.maketrans("", "")
    if not s:
        # Empty files are considered text
        return True
    if "\0" in s:
        # Files with null bytes are likely binary
        return False
    # Get the non-text characters (maps a character to itself then
    # use the 'remove' option to get rid of the text characters.)
    t = s.translate(_null_trans, text_characters)
    # If more than 30% non-text characters, then
    # this is considered a binary file
    if float(len(t))/float(len(s)) > 0.30:
        return False
    return True

def has_lines(filename):



def read_file(path):

    #We don't want anything other than a string!
    assert isinstance(path, basestring)
    assert isinstance(fname, basestring)


    if os.path.isdir(path):
        Printer("That is a dir", i, o, 5)

    elif os.path.isfile(path):
        if is_text(path):
            if has_lines(path):
                f = open(path, 'r')
                flag = 1
                while flag:
                    line = f.getline()
                    Printer(line, i, o, 5)

            else:
                f = open(path, 'r')
                flag = 1
                while flag:
                    line = f.read(20)
                    Printer(line, i, o, 5)
        else:
            Printer("Binary file, danger!", i, o, 5)
            return 1
        
    else:
        Printer("WTF: {}".format(path), i, o, 5) # ;-P
        return 1

    return 0

def browse():
    path_picker = PathPicker("/", i, o, callback=print_path)
    path_picker.activate() #Menu yet to be added
