import logging
logger = logging.getLogger(__name__)

menu_name = "Skeleton app" #App name as seen in main menu while using the system

from subprocess import call
from time import sleep

#had to change this from pyLCI.ui to just ui
#or the import would fail.
from zerophone.ui import Menu, Printer
#from pyLCI.ui.menu import Menu
#from pyLCI.ui.printer import Printer


def call_internal():
    Printer(["Calling internal", "command"], i, o, 1)
    print("Success")

def call_external():
    Printer(["Calling external", "command"], i, o, 1)
    call(['echo', 'Success'])

#Callback global for pyLCI. It gets called when application is activated in the main menu
callback = None

#Some globals for us
i = None #Input device
o = None #Output device

def init_app(input, output):
    global callback, i, o
    i = input; o = output #Getting references to output and input device objects and saving them as globals
    main_menu_contents = [
    ["Internal command", call_internal],
    ["External command", call_external],
    ["Exit", 'exit']]
    main_menu = Menu(main_menu_contents, i, o, "Skeleton app menu")
    callback = main_menu.activate

