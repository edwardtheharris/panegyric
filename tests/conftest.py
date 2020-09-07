#!/usr/bin/env python3

import pytest
import textmywife.text


@pytest.fixture
def text_mw():
    """Return an instance of TextMyWife."""
    return textmywife.text.TextMyWife()


@pytest.fixture
def message():
    """Return message for testing."""
    return {'from': 'harry s truman', 'text': 'the buck stops here'}
