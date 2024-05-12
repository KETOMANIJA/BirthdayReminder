import unittest
from unittest.mock import patch
from BirthdayReminderr import BirthdayReminder, send_reminder
from unittest.mock import MagicMock
class TestSendReminder(unittest.TestCase):
    def test_send_reminder(self):
        reminder = BirthdayReminder("John")
        expected_message = "Nepamiršk nusipirkti saldainių John gimtadieniui!"

        with patch("telebot.TeleBot.send_message") as mock_send_message:
            send_reminder(reminder)
            mock_send_message.assert_called_once_with(6080846508, expected_message)

    def test_handle_callback_query_show_list(self):
        call_mock = MagicMock()
        call_mock.data = 'show_list'
        call_mock.message.chat.id = 6080846508  
    def test_handle_callback_query_show_list(self):
        call_mock = MagicMock()
        call_mock.data = 'add_to_list'
        call_mock.message.chat.id = 6080846508  
    def test_handle_callback_query_show_list(self):
        call_mock = MagicMock()
        call_mock.data = 'remove_from_list'
        call_mock.message.chat.id = 6080846508  
    def test_handle_user_input(self):
        message_mock = MagicMock()
        message_mock.text = 'Vardenis Pavardenssssis, 2000-01-01'
        message_mock.chat.id = 6080846508
class TestHandleCallbackQuery(unittest.TestCase):
    
    def test_handle_user_input(self):  
        message_mock = MagicMock()
        message_mock.text = 'Vardenis Pavardenssssis, 2000-01-01'
        message_mock.chat.id = 6080846508
class TestHandleDeleteInput(unittest.TestCase):
    @patch('builtins.open', MagicMock())
    def test_handle_delete_input_success(self):

        message_mock = MagicMock()
        message_mock.text = 'Robertas Javtokas, 2005-05-04'
        message_mock.chat.id = 6080846508
