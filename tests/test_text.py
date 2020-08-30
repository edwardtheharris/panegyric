#!/usr/bin/env python3

import datetime
import json
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
        assert new_message == message

    def test_api_auth(self, text_mw):
        """Verify authentication with the API."""
        pass

    def test_get_request(self, text_mw):
        """Test that the request is correctly assembled."""
        pass

    def test_api_response(self, text_mw):
        """Validate that the API response is what we expect."""
        pass

    def test_message_iteration(self, text_mw):
        """Test that the same message isn't sent twice."""
        pass

    def test_message_rate(self, text_mw):
        """Verify that we send one message a day."""
        pass
