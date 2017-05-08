'''sends signal commands via subprocess to signal-cli and returns responses
NOTE:  signal-cli must be in your PATH'''

import subprocess
#set up logging
import logging
_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.INFO)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)


def send_message(from_phone_number, to_phone_number, message_body):
    '''sends a text message.  attachments not supported.'''
    _logger.debug('entered send_message')
    _logger.debug('from_phone_number = %s', from_phone_number)
    _logger.debug('to_phone_number = %s', to_phone_number)
    _logger.debug('message_body = %s', message_body)

    args = ["signal-cli", "-u", from_phone_number,
            "send", "-m", message_body, to_phone_number]
    return_string = subprocess.check_output(args, stderr=subprocess.STDOUT)
    _logger.debug('return_string = %s', return_string)
    return return_string

def receive_messages(phone_number):
    '''receives all messages for associated phone number and returns them as a single string'''
    _logger.debug('entered receive_messages')
    _logger.debug('phone_number = %s', phone_number)

    args = ["signal-cli", "-u", phone_number, "receive"]
    messages_as_string = subprocess.check_output(args, stderr=subprocess.STDOUT)
    _logger.debug('messages_as_string = %s', messages_as_string)
    return messages_as_string

def register_phone_number(phone_number):
    '''registers a phone number with signal.
    After registration, you must verify the phone number'''
    _logger.debug('entered register_phone_number')

    args = ["signal-cli", "-u", phone_number, "register"]
    return_string = subprocess.check_output(args, stderr=subprocess.STDOUT)
    _logger.debug('return_string = %s', return_string)
    return return_string

def verify_phone_number(phone_number, verify_code):
    '''verifies a phone number with a verification code'''
    _logger.debug('entered verify_phone_number')
    _logger.debug('phone_number = %s', phone_number)
    _logger.debug('verify_code = %s', verify_code)

    args = ["signal-cli", "-u", phone_number, "verify", verify_code]
    return_string = subprocess.check_output(args, stderr=subprocess.STDOUT)
    _logger.debug('return_string = %s', return_string)
    return return_string
