#!/usr/bin/env python3
"""This module contains the Text class."""
import datetime
import sys

import requests

from ruamel import yaml


class Text:
    """Defines and constructs Text objects."""

    api_key = 'textbelt'
    current_date = None
    message = None
    messages = []
    message_file_path = None
    phone = '0000000000'
    url = 'https://textbelt.com/text'

    def __init__(self, message_file_path):
        """Initialize a Text instance."""
        self.current_date = datetime.datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0)
        self.message_file_path = message_file_path

    def get_message(self):
        """Get a message to send."""
        all_messages = self.messages
        least_recent_date = None
        message = None

        for message_item in all_messages:
            least_recent_date = self.check_send_date(
                message_item, least_recent_date)
            if (
                    least_recent_date <= self.current_date
                    and message is None):
                current_date_str = datetime.datetime.strftime(
                    self.current_date, '%Y-%m-%d'
                )
                message_item.update(
                    {'send_date': current_date_str})
                message = message_item
        self.write_messages()
        return message

    def check_send_date(self, message, least_recent_date):
        """Check that this is least recently sent message."""
        if (message.get('send_date')
                and least_recent_date is None):
            least_recent_date = datetime.datetime.strptime(
                message.get('send_date'), '%Y-%m-%d')
        elif (message.get('send_date')
                and least_recent_date is not None):
            send_date = datetime.datetime.strptime(
                message.get('send_date'), '%Y-%m-%d')
            if least_recent_date > send_date:
                least_recent_date = send_date
        else:
            least_recent_date = self.current_date
        return least_recent_date

    def get_all_messages(self):
        """Get all messages."""
        yml = yaml.YAML(typ='safe', pure=True)
        self.messages = yml.load(
            open(self.message_file_path))
        return self.messages

    def send_message(self):
        """Send the selected message."""
        text_from = self.message.get('from')
        text_text = self.message.get('text')

        message_dict = {
            'phone': self.phone,
            'message': f'{text_text} - {text_from}',
            'key': self.api_key,
        }

        resp = requests.post(self.url, message_dict)
        return resp

    def write_messages(self):
        """Write updated messages message list."""
        yml = yaml.YAML()
        yml.dump(self.messages, sys.stdout)
        yml.dump(self.messages, open(self.message_file_path, 'w'))


def main():
    """Execute main program."""
    text = Text('src/compliments/work-card.yaml')
    text.get_all_messages()
    text.message = text.get_message()
    text.api_key = "textbelt_test"
    result = text.send_message()
    print(result.__dict__)


if __name__ == '__main__':
    main()
