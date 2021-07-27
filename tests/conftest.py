#!/usr/bin/env python3
"""Configuration for panegyric tests."""

import pytest
import panegyric.text


@pytest.fixture
def text():
    """Return an instance of TextMyWife."""
    return panegyric.text.Text()


@pytest.fixture
def message():
    """Return message for testing."""
    return {'from': 'harry s truman', 'text': 'the buck stops here'}
