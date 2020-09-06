#!/usr/bin/env python3

import datetime
import json
import os
import dotenv
import requests
import textmywife


class TestTextMyWife:
    """Test class for text my wife package."""

    def test_get_message(self, text_mw):
        """Test message retrival."""
        message = text_mw.get_message('tests/compliments.yml')
        assert isinstance(message, dict)
        assert json.dumps(message)
        assert message.get('from') == 'billybuck'
        assert message.get('text') == 'You have very nice hair.'

    def test_add_send_date(self, text_mw, message):
        """Test recording of most recent send date."""
        current_date = datetime.date.today()
        message.update(
            {'send_date': datetime.date.strftime(current_date, '%Y-%m-%d')})
        new_message = text_mw.add_send_date()

        assert isinstance(message, dict)
        assert json.dumps(message)
        assert message.get('from') == 'harry s truman'
        assert message.get('text') == 'the buck stops here'
        assert message.get('send_date') == datetime.date.strftime(
            current_date, '%Y-%m-%d')
        assert new_message == message

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

    def test_message_iteration(self, text_mw):
        """Test that the same message isn't sent twice."""
        tmw_instance = textmywife.TextMyWife()
        assert isinstance(tmw_instance, textmywife.TextMyWife)
        pass

    def test_message_rate(self, text_mw):
        """Verify that we send one message a day."""
        test_current_date = datetime.datetime.strptime(
            '%Y-%m-%d', '2020-09-06')
        with open('date-last-sent') as date_last_sent_fh:
            date_last_sent_str = date_last_sent_fh.read()

        date_last_sent = datetime.datetime.strptime(
            '%Y-%m-%d', date_last_sent_str)

        assert date_last_sent == test_current_date
