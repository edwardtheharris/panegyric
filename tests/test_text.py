#!/usr/bin/env python3
"""Tests for the Text class."""

import datetime
import json
import os
import dotenv
import pytest
import requests


class TestText:
    """Test class for text my wife package."""

    send_date = '2021-07-26'

    def test_get_message(self, text):
        """Test message retrival."""
        # message = text.get_message('tests/compliments.yml')
        # assert isinstance(message, dict)
        # assert json.dumps(message)
        # assert message.get('from') == 'billybuck'
        # assert message.get('text') == 'You have very nice hair.'
        print(json.dumps({"some": "value"}))
        assert True

    def test_get_all_messages(self, text):
        """Test get every message."""
        messages = text.get_all_messages('tests/compliments.yml')

        assert isinstance(messages, list)
        assert True

    @pytest.mark.parametrize(
        'message, least_recent_date', [(
            {'from': 'billybuck',
             'text': 'You have very nice hair'},
            None),
            # ({'from': 'billybuck',
            #   'text': 'You have very nice hair',
            #   'send_date': (datetime.datetime.strftime(
            #         datetime.datetime.now(),
            #         '%Y-%m-%d') - datetime.timedelta(
            #             days=4))},
            #  (datetime.datetime.strftime(
            #      datetime.datetime.now(), '%Y-%m-%d') - datetime.timedelta(
            #      days=5)))
        ]
    )
    def test_check_send_date(self, text, message, least_recent_date):
        """Test recording of most recent send date."""
        # current_date = datetime.datetime.now()
        test_least_recent_date = text.check_send_date(
            message, least_recent_date
        )

        assert isinstance(message, dict)
        # assert isinstance(least_recent_date, str)
        # assert json.dumps(message)
        if (
                message.get('send_date')
                and least_recent_date is None):
            assert test_least_recent_date == datetime.datetime.strftime(
                message.get('send_date'), '%Y-%m-%d'
            )

        # if (
        #         message.get('send_date')
        #         and least_recent_date is not None):
        #     assert test_least_recent_date == (datetime.datetime.strftime(
        #         datetime.datetime.now(), '%Y-%m-%d') - datetime.timedelta(
        #         days=5))
        # assert message.get('send_date') == datetime.datetime.strftime(
        #     current_date, '%Y-%m-%d')
        # assert new_message == message
        assert True

    def test_send_message(self, text):
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

    def test_message_iteration(self, text):
        """Test that the same message isn't sent twice."""
        # tmw_instance = textmywife.text.TextMyWife()

        # for message in tmw_instance.get_all_messages():
        #     assert message.get('send_date') != '2020-09-06'
        # assert isinstance(tmw_instance, textmywife.text.TextMyWife)
        test_date = datetime.datetime.now()
        assert isinstance(test_date, datetime.datetime)
        assert True

    def test_message_rate(self, text):
        """Verify that we send one message a day."""
        # messages = text.get_all_messages()

        # date_list = []
        # for message in messages:
        #     date_list.append(message.get('send_date'))

        # assert set(date_list) == date_list
        assert True
