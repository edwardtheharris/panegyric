#!/usr/bin/env python3

import pytest
import textmywife


@pytest.fixture
def text_mw():
    """Return an instance of TextMyWife."""
    return textmywife.TextMyWife()


@pytest.fixture
def message():
    """Return message for testing."""
    return {'from': 'harry s truman', 'text': 'the buck stops here'}
