'''tests signal-cli functionality.  this will be used to create a zerophone app'''
import subprocess
import unittest
import time
from datetime import datetime
import logging
import zerophone.apps.signal.main

#set up logging

_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.DEBUG)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)

SENDER_PHONE_NUMBER = "+15304548041"
RECEIVER_PHONE_NUMBER = "+13513331152"
#this phone number was created during testing of register/verify
EXTRA_PHONE_NUMBER = "+13513331154"

class TestSignalApp(unittest.TestCase):
    '''tests the use of signal-cli via the subprocess module in python.
       this will be used in building a signal app in the zerophone'''

    def test_echo(self):
        '''tests python subprocess of echoing a simple string'''
        string_to_echo = "Hello World!"
        return_string = subprocess.check_output(["echo", string_to_echo])
        _logger.debug('return_string = %s', return_string)
        #echo adds a line feed to the input string.  who knew.
        self.assertEqual(string_to_echo + '\n', return_string)

    def test_signal_send_message(self):
        '''tests sending a single signal text message, no attachments'''
        _logger.debug('entered test_signal_send_message')
        time_stamp = str(datetime.now())
        message_body = "a most excellently constructed message built at {0}".format(time_stamp)
        _logger.debug('message_body = %s', message_body)

        return_string = zerophone.apps.signal.main.send_message(
            SENDER_PHONE_NUMBER, RECEIVER_PHONE_NUMBER, message_body)
        self.assertEqual('', return_string)

    def test_signal_receive(self):
        '''tests signal receiving message(s), assumes one has already been sent
           so there is something to receive'''
        _logger.debug('entered test_signal_receive')
        #/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 receive

        return_string = zerophone.apps.signal.main.receive_messages(RECEIVER_PHONE_NUMBER)
        self.assertNotEqual('', return_string)

    def test_signal_send_and_receive(self):
        '''tests sending and receiving a messsage,
        this allows verification the message body didn't change when transmitted through Signal'''
        _logger.debug('entered test_signal_send_and_receive')
        time_stamp = str(datetime.now())
        message_body = "a most excellently constructed message built at {0}".format(time_stamp)
        _logger.debug('message_body = %s', message_body)
        send_return_string = zerophone.apps.signal.main.send_message(
            SENDER_PHONE_NUMBER, RECEIVER_PHONE_NUMBER, message_body)
        self.assertEqual('', send_return_string)
        time.sleep(2)
        receive_return_string = zerophone.apps.signal.main.receive_messages(RECEIVER_PHONE_NUMBER)
        _logger.debug('receive_return_string = %s', receive_return_string)
        self.assertIn(message_body, receive_return_string)

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
        #/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 register
        command_to_execute = "/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli"
        args = [command_to_execute, "-u", new_phone_number, "register"]
        return_string = subprocess.check_output(args)
        _logger.debug('return_string = %s', return_string)
        self.assertEqual('', return_string)

    def test_signal_verify(self):
        '''tests verifying a phone number with a Signal verification code'''
        _logger.debug('entered test_signal_verify')
        #/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 verify 627-717
        phone_number = "+13513331154"
        verify_code = "803-071"
        command_to_execute = "/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli"
        args = [command_to_execute, "-u", phone_number, "verify", verify_code]
        return_string = subprocess.check_output(args)
        _logger.debug('return_string = %s', return_string)
        self.assertEqual('', return_string)
