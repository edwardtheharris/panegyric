#!/usr/bin/env python3
# pylint: disable=E0401
"""Tests for the Text class.

import os
"""
import datetime
import json
import pathlib

from unittest.mock import patch
from unittest.mock import Mock

import pytest
import requests

from ruamel.yaml import YAML

from panegyric.text import main
from panegyric.text import Text


class TestText:
    """Test class for Text class.

    # from pytest_sentry import Client
    # @pytest.mark.sentry_client(Client({
    #     'dsn': os.environ.get('PYTEST_SENTRY_DSN'),
    #     'debug': True}
    # ))
    """

    send_date = (datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) - datetime.timedelta(days=5))

    def test_init(self):
        """Test instantiation of the class."""
        text = Text('tests/compliments.yml')
        assert isinstance(text, Text)

    def test_get_message(self):
        """Test message retrival."""
        text = Text('tests/compliments.yml')
        text.messages = text.get_all_messages()
        text.message_file_path = 'tests/result/compliments.yml'
        test_message = text.get_message()

        assert isinstance(test_message, dict)
        assert json.dumps(test_message)
        assert test_message.get('from') == 'billybuck'
        assert test_message.get('text') == 'You have very nice hair'

        text = Text('tests/result/compliments.yml')
        text.messages = text.get_all_messages()
        test_message = text.get_message()

        yml = YAML()
        cmp_yml = pathlib.Path('tests/result/compliments.yml')
        with cmp_yml.open('r', encoding='utf-8') as cmp_fh:
            test_data = yml.load(cmp_fh)
        assert text.messages == test_data
        assert isinstance(test_message, dict)
        assert json.dumps(test_message)
        assert test_message.get('from') == 'billybuck'
        assert test_message.get('text') == 'You have very nice hair'

    def test_get_all_messages(self, messages):
        """Test get every message."""
        text = Text('tests/compliments.yml')
        test_messages = text.get_all_messages()

        assert isinstance(messages, list)
        assert test_messages == messages

    @ pytest.mark.parametrize(
        'message, least_recent_date', [(
            {'from': 'billybuck',
             'text': 'You have very nice hair'},
            None),
            ({'from': 'billybuck',
              'text': 'You have very nice hair',
              'send_date': datetime.datetime.strftime(
                  datetime.datetime.now().replace(
                      hour=0, minute=0, second=0, microsecond=0
                  ) - datetime.timedelta(days=5), '%Y-%m-%d'
              )},
             (datetime.datetime.now().replace(
                 hour=0, minute=0, second=0, microsecond=0
             ) - datetime.timedelta(days=5)))
        ]
    )
    def test_check_send_date(self, message, least_recent_date):
        """Test recording of most recent send date."""
        text = Text('test/compliments.yml')
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

    @ patch('requests.post')
    def test_send_message(self, mocked_post):
        """Validate that the API response is what we expect."""
        text = Text('tests/fixtures/compliments-no-date.yml')
        text.messages = text.get_all_messages()
        text.message_file_path = 'tests/fixtures/compliments-with-date.yml'
        text_message = text.get_message()
        text_from = text_message.get('from')
        text_text = text_message.get('text')
        test_key = text.api_key

        message_dict = {
            'phone': '2138765309',
            'message': f'{text_text} - {text_from}',
            'key': f'{test_key}_test ',
        }
        rsp = pathlib.Path('tests/fixtures/resp.json')
        with rsp.open('r', encoding='utf-8') as rsp_fh:
            response_dict = json.load(rsp_fh)
        mocked_post.return_value = Mock(
            status_code=200,
            json=lambda: response_dict)
        resp = requests.post(text.url, message_dict, timeout='60s')

        assert resp.status_code == 200
        assert isinstance(resp.json(), dict)
        assert response_dict == resp.json()

    def test_write_messages(self):
        """Test update of message file."""
        text = Text('tests/compliments.yml')
        text.messages = text.get_all_messages()
        text.write_messages()

        yml = YAML()
        cmp_yml = pathlib.Path('tests/compliments.yml')
        with cmp_yml.open('r', encoding='utf-8') as cmp_fh:
            test_data = yml.load(cmp_fh)
        assert text.messages == test_data

    def test_message_rate(self):
        """Verify that we send one message a day."""
        text = Text('tests/fixtures/compliments-duplicate-date.yml')
        text.messages = text.get_all_messages()
        text.message = text.get_message()

        test_send_date = (datetime.datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        ))

        message_send_date = datetime.datetime.strptime(
            text.message.get('send_date'), '%Y-%m-%d')

        assert message_send_date <= test_send_date

    def test_main(self):
        """Test main program execution."""
        test_result = main()
        assert test_result.status_code == 200
