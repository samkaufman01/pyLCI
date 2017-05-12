'''tests signal-cli functionality.  this will be used to create a zerophone app'''
import subprocess
import unittest
import time
from datetime import datetime
import logging
import zerophone.apps.signal.signal_cli_commands

#set up logging

_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.DEBUG)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)

SENDER_PHONE_NUMBER = "+15304548041"
RECEIVER_PHONE_NUMBER = "+13513331152"
#this phone number was registered during testing of register/verify
EXTRA_PHONE_NUMBER = "+13513331154"

class TestSignalCli(unittest.TestCase):
    '''tests the use of signal-cli via the subprocess module in python.
       this will be used in building a signal app in the zerophone'''

    def test_echo(self):
        '''tests python subprocess of echoing a simple string'''
        string_to_echo = "Hello World!"
        args = ["echo", string_to_echo]
        return_string = subprocess.check_output(args, stderr=subprocess.STDOUT)
        _logger.debug('return_string = %s', return_string)
        #echo adds a line feed to the input string.  who knew.
        self.assertEqual(string_to_echo + '\n', return_string)

    def test_signal_get_version(self):
        '''tests ability to run signal-cli -v and get version.
           if this fails, signal-cli is likely not in PATH'''
        _logger.debug('entered test_signal_get_version')
        args = ["signal-cli", "-v"]
        return_string = subprocess.check_output(args, stderr=subprocess.STDOUT)
        _logger.debug('return_string = %s', return_string)
        self.assertEqual(return_string, 'signal-cli 0.5.5\n', "Is signal-cli in your PATH?")

    def test_signal_send_message(self):
        '''tests sending a single signal text message, no attachments'''
        _logger.debug('entered test_signal_send_message')
        time_stamp = str(datetime.now())
        message_body = "a most excellently constructed message built at {0}".format(time_stamp)
        _logger.debug('message_body = %s', message_body)

        return_string = zerophone.apps.signal.signal_cli_commands.send_message(
            SENDER_PHONE_NUMBER, RECEIVER_PHONE_NUMBER, message_body)
        self.assertEqual('', return_string)

    def test_signal_receive(self):
        '''tests signal receiving message(s), assumes one has already been sent
           so there is something to receive'''
        _logger.debug('entered test_signal_receive')

        return_string = zerophone.apps.signal.signal_cli_commands.receive_messages(
            RECEIVER_PHONE_NUMBER)
        self.assertNotEqual('', return_string)

    def test_signal_send_and_receive(self):
        '''tests sending and receiving a messsage,
        this allows verification the message body didn't change when transmitted through Signal'''
        _logger.debug('entered test_signal_send_and_receive')
        time_stamp = str(datetime.now())
        message_body = "a most excellently constructed message built at {0}".format(time_stamp)
        _logger.debug('message_body = %s', message_body)
        send_return_string = zerophone.apps.signal.signal_cli_commands.send_message(
            SENDER_PHONE_NUMBER, RECEIVER_PHONE_NUMBER, message_body)
        self.assertEqual('', send_return_string)
        time.sleep(2)
        receive_return_string = \
            zerophone.apps.signal.signal_cli_commands.receive_messages(RECEIVER_PHONE_NUMBER)
        _logger.debug('receive_return_string = %s', receive_return_string)
        self.assertIn(message_body, receive_return_string)

    @unittest.skip("skip registering numbers until there is an automated way to get verify codes")
    def test_signal_register(self):
        '''tests registering a new phone number with signal.
            the phone number must be able to receive an sms.
            the phone number can only be registered once.
            After sending the register request, an SMS with a Signal
            verification code will be sent to the phone.
            Use the Signal verification code (quickly) to verify
            the phone number'''
        _logger.debug('entered test_signal_register')
        #make sure to include the + sign at the beginning of the phone number
        new_phone_number = "+13513331154"
        return_string = zerophone.apps.signal.signal_cli_commands.register_phone_number(
            new_phone_number)
        self.assertEqual('', return_string)

    @unittest.skip("skip registering numbers until there is an automated way to get verify codes")
    def test_signal_verify(self):
        '''tests verifying a phone number with a Signal verification code'''
        _logger.debug('entered test_signal_verify')
        phone_number = "+13513331154"
        verify_code = "694-676"
        return_string = zerophone.apps.signal.signal_cli_commands.verify_phone_number(
            phone_number, verify_code)
        self.assertEqual('', return_string)
