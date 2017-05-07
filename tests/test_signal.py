'''tests signal app'''
import subprocess
import unittest
import time
from datetime import datetime
import zerophone.apps.signal.main

#set up logging
import logging
_LOG_FORMAT = '%(levelname)s %(asctime)-15s %(name)s  %(message)s'
logging.basicConfig(format=_LOG_FORMAT, level=logging.DEBUG)
_logger = logging.getLogger(__name__)
_logger.debug('executing name %s in file %s', __name__, __file__)

class TestSignalApp(unittest.TestCase):
    '''tests a simple subprocess version of signal messenger
       using the signal-cli interface'''

    def test_echo(self):
        '''tests subprocess of echoing a simple string'''
        string_to_echo = "Hello World!"
        return_string = subprocess.check_output(["echo", string_to_echo])
        _logger.debug('return_string = %s', return_string)
        self.assertEqual(string_to_echo + '\n', return_string)

    def test_signal_send_message(self):
        '''tests sending a single signal text message, no attachments'''
        _logger.debug('entered test_signal_send_message')
        time_stamp = str(datetime.now())
        message_body = "a most excellently constructed message built at {0}".format(time_stamp)
        _logger.debug('message_body = %s', message_body)
        sender_phone_number = "+15304548041"
        receiver_phone_number = "+13513331152"
        return_string = zerophone.apps.signal.main.send_message(
            sender_phone_number, receiver_phone_number, message_body)
        self.assertEqual('', return_string)

    def test_signal_receive(self):
        '''tests signal receiving message, assumes one has already been sent
           so there is something to receive'''
        _logger.debug('entered test_signal_receive')
        #/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 receive
        phone_number = "+13513331152"
        return_string = zerophone.apps.signal.main.receive_messages(phone_number)
        self.assertNotEqual('', return_string)

    def test_signal_send_and_receive(self):
        '''tests sending and receiving a messsage,
        this allows verification the message body didn't change'''
        _logger.debug('entered test_signal_send_and_receive')
        time_stamp = str(datetime.now())
        message_body = "a most excellently constructed message built at {0}".format(time_stamp)
        _logger.debug('message_body = %s', message_body)
        sender_phone_number = "+15304548041"
        receiver_phone_number = "+13513331152"
        send_return_string = zerophone.apps.signal.main.send_message(
            sender_phone_number, receiver_phone_number, message_body)
        self.assertEqual('', send_return_string)
        time.sleep(2)
        receive_return_string = zerophone.apps.signal.main.receive_messages(receiver_phone_number)
        _logger.debug('receive_return_string = %s', receive_return_string)
        self.assertIn(message_body, receive_return_string)
