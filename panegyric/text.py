#!/usr/bin/env python3
"""This module contains the Text class."""
import datetime
from ruamel import yaml


class Text:
    """Defines and constructs Text objects."""

    current_date = None
    message = None
    messages = []

    def __init__(self):
        """Initialize a Text instance."""
        self.current_date = datetime.datetime.now()

    def get_message(self):
        """Get a message to send."""
        all_messages = self.messages
        least_recent_date = None
        message = None

        for message_item in all_messages:
            print(message_item)
            least_recent_date = self.check_send_date(
                message_item, least_recent_date)
            if least_recent_date <= self.current_date:
                current_date_str = datetime.datetime.strftime(
                    self.current_date, '%Y-%m-%d'
                )
                message = message_item.update(
                    {'send_date': current_date_str})

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
            least_recent_date = datetime.datetime.now()
        return least_recent_date

    def get_all_messages(self, message_file_location):
        """Get all messages."""
        yml = yaml.YAML(typ='safe', pure=True)
        messages = yml.load(
            open(message_file_location))
        return messages

    def send_message(self):
        """Send the selected message."""
        return

    def iterate_message(self):
        """Iterate message list."""
        return


def main():
    """Execute main program."""
    text = Text()
    text.messages = text.get_messages(
        'compliments/work-card.yaml')
    text.get_message()
    print(text.messages)


if __name__ == '__main__':
    main()
