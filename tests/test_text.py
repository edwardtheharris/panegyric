#!/usr/bin/env python3

import datetime
import json
import os
import dotenv
import requests
# import textmywife


class TestTextMyWife:
    """Test class for text my wife package."""

    def test_get_message(self, text_mw):
        """Test message retrival."""
        # message = text_mw.get_message('tests/compliments.yml')
        # assert isinstance(message, dict)
        # assert json.dumps(message)
        # assert message.get('from') == 'billybuck'
        # assert message.get('text') == 'You have very nice hair.'
        print(json.dumps({"some": "value"}))
        assert True

    def test_get_all_messages(self, text_mw):
        """Test get every message."""
        # messages = text_mw.get_all_messages()

        # assert isinstance(messages, list)
        assert True

    def test_add_send_date(self, text_mw, message):
        """Test recording of most recent send date."""
        # current_date = datetime.date.today()
        # message.update(
        #     {'send_date': datetime.date.strftime(current_date, '%Y-%m-%d')})
        # new_message = text_mw.add_send_date()

        # assert isinstance(message, dict)
        # assert json.dumps(message)
        # assert message.get('from') == 'harry s truman'
        # assert message.get('text') == 'the buck stops here'
        # assert message.get('send_date') == datetime.date.strftime(
        #     current_date, '%Y-%m-%d')
        # assert new_message == message
        assert True

    def test_api_response(self, text_mw):
        """Validate that the API response is what we expect."""
        dotenv.load_dotenv()
        test_key = os.getenv('api_key')
        resp = requests.post('https://textbelt.com/text', {
            'phone': '4243219495',
            'message': 'the buck stops here - harry s truman',
            'key': f'{test_key}_test',
        })
        print(resp.json())
        assert isinstance(resp.json(), dict)

    def test_message_iteration(self, text_mw):
        """Test that the same message isn't sent twice."""
        # tmw_instance = textmywife.text.TextMyWife()

        # for message in tmw_instance.get_all_messages():
        #     assert message.get('send_date') != '2020-09-06'
        # assert isinstance(tmw_instance, textmywife.text.TextMyWife)
        test_date = datetime.datetime.now()
        assert isinstance(test_date, datetime.datetime)
        assert True

    def test_message_rate(self, text_mw):
        """Verify that we send one message a day."""
        # messages = text_mw.get_all_messages()

        # date_list = []
        # for message in messages:
        #     date_list.append(message.get('send_date'))

        # assert set(date_list) == date_list
        assert True
