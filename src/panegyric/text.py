#!/usr/bin/env python3
"""This module contains the Text class."""
import datetime
import pprint
import sys

import requests
import sentry_sdk

from ruamel import yaml


class Text:
    """Defines and constructs Text objects.

    :param str message_file_path: Path to the file containing messages.
    """

    #: The API key to use for sending texts.
    api_key = 'textbelt'
    #: The date of execution.
    current_date = None
    #: The message to send.
    message = None
    #: All of the messages that can be sent.
    messages = []
    #: Path to a yaml file containing messages.
    message_file_path = None
    #: Phone number to send to.
    phone = '0000000000'
    #: The url for the text sending service.
    url = 'https://textbelt.com/text'

    def __init__(self, message_file_path):
        """Initialize a Text instance.

        :param str message_file_path: Path to the file containing messages.
        """
        self.current_date = datetime.datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0)
        self.message_file_path = message_file_path
        sentry_sdk.init(
            ("https://a40e278a662e46db86ef8aa4d7a46fbd@o325200"
             ".ingest.sentry.io/5955114"),

            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0
        )

    def get_message(self):
        """Get a message to send.

        :ivar dict all_messages: All of the messages.
        :ivar datetime.datetime least_recent_date: Oldest message send.
        :ivar str message: Message to send.
        """
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
        """Check that this is least recently sent message.

        :param str message: Message to check the date of.
        :param datetime.datetime least_recent_date: Oldest sned for a message.
        """
        if (message.get('send_date')
                and least_recent_date is None):
            least_recent_date = datetime.datetime.strptime(
                message.get('send_date'), '%Y-%m-%d')
        elif (message.get('send_date')
                and least_recent_date is not None):
            send_date = datetime.datetime.strptime(
                message.get('send_date'), '%Y-%m-%d')
            least_recent_date = min(least_recent_date, send_date)
        else:
            least_recent_date = self.current_date
        return least_recent_date

    def get_all_messages(self):
        """Get all messages.

        :ivar ruamel.yaml.YAML yml: A YAML object to parse messages.
        """
        yml = yaml.YAML(typ='safe', pure=True)
        with open(self.message_file_path, 'r', encoding='utf-8') as mfp_fh:
            self.messages = yml.load(mfp_fh)
        return self.messages

    def send_message(self):
        """Send the selected message.

        :ivar str text_from: Message from.
        :ivar str text_text: Message text.
        :ivar dict message_dict: Dictionary with payload.
        :ivar requests.Response resp: Response from API.
        """
        text_from = self.message.get('from')
        text_text = self.message.get('text')

        message_dict = {
            'phone': self.phone,
            'message': f'{text_text} - {text_from}',
            'key': self.api_key,
        }

        resp = requests.post(self.url, message_dict, timeout=60)
        return resp

    def write_messages(self):
        """Write updated messages message list.

        :ivar ruamel.yaml.YAML yml: A yaml object to write messages.
        """
        yml = yaml.YAML()
        yml.dump(self.messages, sys.stdout)
        with open(self.message_file_path, 'w', encoding='utf-8') as mfp_fh:
            yml.dump(self.messages, mfp_fh)


def main():
    """Execute main program.

    :ivar Text text: The Text object.
    :ivar requests.Response result: Response object.
    """
    text = Text('src/compliments/work-card.yaml')
    text.get_all_messages()
    text.message = text.get_message()
    text.api_key = "textbelt_test"
    result = text.send_message()
    pprint.pprint(result.__dict__)
    return result


if __name__ == '__main__':
    main()
