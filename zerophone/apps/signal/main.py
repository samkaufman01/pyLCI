'''signal app, uses signal-cli under the hood'''
import subprocess
import logging
from zerophone.ui import Menu
from zerophone.ui import Printer
import zerophone.apps.signal

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
    i = input; o = output

def send_message_callback():
    '''menu callback, triggered when user chooses send message'''
    _logger.debug('entered send_message_callback')
    SENDER_PHONE_NUMBER = "+15304548041"
    RECEIVER_PHONE_NUMBER = "+13513331152"
    message_body = "hello zerophone world"
    zerophone.apps.signal.main.send_message(
        SENDER_PHONE_NUMBER, RECEIVER_PHONE_NUMBER, message_body)
    Printer("sent message", i, o)

def receive_message_callback():
    '''menu callback, triggered when user chooses receive message'''
    _logger.debug('entered receive_message_callback')
    Printer("received messages", i, o)

def show_menu():
    '''shows the menu for the signal app'''
    _logger.debug('entered show_menu')
    menu_contents = []
    menu_contents.append(["send message", send_message_callback])
    menu_contents.append(["receive message(s)", receive_message_callback])
    Menu(menu_contents, i, o, entry_height=2).activate()

#this statement must be below the function definition for show_menu
#or the menu will fail to load
callback = show_menu

def send_message(from_phone_number, to_phone_number, message_body):
    '''sends a text message.  attachments not supported.'''
    _logger.debug('entered send_message')
    _logger.debug('from_phone_number = %s', from_phone_number)
    _logger.debug('to_phone_number = %s', to_phone_number)
    _logger.debug('message_body = %s', message_body)

    command_to_execute = "/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli"
    args = [command_to_execute, "-u", from_phone_number,
            "send", "-m", message_body, to_phone_number]
    return_string = subprocess.check_output(args)
    _logger.debug('return_string = %s', return_string)
    return return_string

def receive_messages(phone_number):
    '''receives all messages for associated phone number and returns them as a single string'''
    _logger.debug('entered receive_messages')
    _logger.debug('phone_number = %s', phone_number)

    command_to_execute = "/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli"
    args = [command_to_execute, "-u", phone_number, "receive"]
    messages_as_string = subprocess.check_output(args)
    _logger.debug('messages_as_string = %s', messages_as_string)
    return messages_as_string
