'''signal app, uses signal-cli under the hood'''

import logging
from zerophone.ui import Menu
from zerophone.ui import Printer
import zerophone.apps.signal.signal_cli_commands

#set up logging
_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.DEBUG)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)

menu_name = "Signal"
i = None
o = None

def init_app(input, output):
    global i, o
    i = input
    o = output

def send_message_menu_callback():
    '''menu callback, triggered when user chooses send message'''
    _logger.debug('entered send_message_callback')
    #TODO:  these arguments need to come from the UI
    SENDER_PHONE_NUMBER = "+15304548041"
    RECEIVER_PHONE_NUMBER = "+13513331152"
    message_body = "hello zerophone world"
    zerophone.apps.signal.signal_cli_commands.send_message(
        SENDER_PHONE_NUMBER, RECEIVER_PHONE_NUMBER, message_body)
    Printer("sent message", i, o)

def receive_message_menu_callback():
    '''menu callback, triggered when user chooses receive message'''
    _logger.debug('entered receive_message_callback')
    Printer("received messages", i, o)

def show_menu_callback():
    '''shows the menu for the signal app'''
    _logger.debug('entered show_menu_callback')
    menu_contents = []
    menu_contents.append(["send message", send_message_menu_callback])
    menu_contents.append(["receive message(s)", receive_message_menu_callback])
    Menu(menu_contents, i, o, entry_height=2).activate()

#this statement must be below the function definition for show_menu
#or the menu will fail to load
callback = show_menu_callback


