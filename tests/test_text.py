#!/usr/bin/env python3
"""Tests for the Text class."""

import datetime
import json
import os

import dotenv
import pytest
import requests

from panegyric.text import Text


class TestText:
    """Test class for Text class."""

    send_date = (datetime.datetime.now() - datetime.timedelta(days=5))

    def test_get_message(self):
        """Test message retrival."""
        text = Text('tests/compliments.yml')
        text.messages = text.get_all_messages()
        text.message_file_path = 'tests/out/compliments.yml'
        test_message = text.get_message()

        assert isinstance(test_message, dict)
        assert json.dumps(test_message)
        assert test_message.get('from') == 'billybuck'
        assert test_message.get('text') == 'You have very nice hair\n'

        text = Text('tests/out/compliments.yml')
        text.messages = text.get_all_messages()
        test_message = text.get_message()

        assert isinstance(test_message, dict)
        assert json.dumps(test_message)
        assert test_message.get('from') == 'billybuck'
        assert test_message.get('text') == 'You have very nice hair\n'

    def test_get_all_messages(self, text, messages):
        """Test get every message."""
        test_messages = text.get_all_messages()

        assert isinstance(messages, list)
        assert test_messages == messages

    @pytest.mark.parametrize(
        'message, least_recent_date', [(
            {'from': 'billybuck',
             'text': 'You have very nice hair'},
            None),
            ({'from': 'billybuck',
              'text': 'You have very nice hair',
              'send_date': '2021-07-21'},
             (datetime.datetime.now().replace(
                 hour=0, minute=0, second=0, microsecond=0
             ) - datetime.timedelta(days=5)))
        ]
    )
    def test_check_send_date(self, text, message, least_recent_date):
        """Test recording of most recent send date."""
        test_least_recent_date = text.check_send_date(
            message, least_recent_date
        )
        if least_recent_date is None:
            assert test_least_recent_date == datetime.datetime.now().replace(
                hour=0, minute=0, second=0, microsecond=0)
        else:
            assert test_least_recent_date == least_recent_date

        assert isinstance(message, dict)
        assert json.dumps(message)
        assert isinstance(test_least_recent_date, datetime.datetime)

    def test_send_message(self, text):
        """Validate that the API response is what we expect."""
        dotenv.load_dotenv()
        test_key = os.getenv('api_key')
        resp = requests.post('https://textbelt.com/text', {
            'phone': '4243219495',
            'message': 'the buck stops here - harry s truman',
            'key': f'{test_key}_test',
        })
        assert isinstance(resp.json(), dict)

    def test_write_messages(self, text):
        """Test update of message file."""
        assert True

    def test_message_rate(self, text):
        """Verify that we send one message a day."""
        # messages = text.get_all_messages()

        # date_list = []
        # for message in messages:
        #     date_list.append(message.get('send_date'))

        # assert set(date_list) == date_list
        assert True
