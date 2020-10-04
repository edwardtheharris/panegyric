#!/usr/bin/env python3
from ruamel import yaml


class TextMyWife:
    def __init__(self):
        """Initialize a TextMyWife instance."""
        pass

    def get_message(self):
        """Get a message to send."""
        return

    def get_all_messages(self, message_file_location):
        """Get all messages."""
        messages = yaml.safe_load(
            open(message_file_location))
        return messages

    def add_send_date(self):
        """Append most recent send date."""
        return

    def send_message(self):
        """Send the selected message."""
        return

    def iterate_message(self):
        """Iterate message list."""
        return


def main():
    """Main program execution."""
    text_mw = TextMyWife()
    messages = text_mw.get_messages('compliments/work-card.yaml')
    print(messages)


if __name__ == '__main__':
    main()
