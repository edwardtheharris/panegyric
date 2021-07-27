#!/usr/bin/env python3
import datetime
from ruamel import yaml


class TextMyWife:
    message = None
    messages = []

    def __init__(self):
        """Initialize a TextMyWife instance."""
        pass

    def get_message(self):
        """Get a message to send."""
        all_messages = self.messages
        current_date = datetime.datetime.strptime(
            '%Y-%m-%d', datetime.datetime.now()
        )
        least_recent_date = None
        message = None

        for message_item in all_messages:
            least_recent_date = self.check_send_date(
                message_item, least_recent_date)
            if least_recent_date <= current_date:
                message = message_item.update(
                    {'send_date': current_date})

        return message

    def check_send_date(self, message, least_recent_date):
        """Check that this is least recently sent message.

        'But polymorphism is way better,' blah blah; we
        just want it to fucking work right now. I'll write
        a dispatch method later.
        """
        if (
                message.get('send_date')
                and least_recent_date is None
        ):
            least_recent_date = datetime.datetime.strptime(
                message.get('send_date'), '%Y-%m-%d')
        elif (
                message.get('send_date')
                and least_recent_date is not None
        ):
            send_date = datetime.datetime.strftime(
                message.get('send_date'), '#Y-#m-#d')
            if least_recent_date > send_date:
                least_recent_date = send_date
        else:
            least_recent_date = datetime.datetime.strftime(
                '%Y-%m-%d', datetime.datetime.now())
        return least_recent_date

    def get_all_messages(self, message_file_location):
        """Get all messages."""
        messages = yaml.safe_load(
            open(message_file_location))
        return messages

    def send_message(self):
        """Send the selected message."""
        return

    def iterate_message(self):
        """Iterate message list."""
        return


def main():
    """Main program execution."""
    text_mw = TextMyWife()
    text_mw.messages = text_mw.get_messages(
        'compliments/work-card.yaml')
    text_mw.get_message()
    print(text_mw.messages)


if __name__ == '__main__':
    main()
