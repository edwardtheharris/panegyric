#!/usr/bin/env python3
"""Configuration for panegyric tests."""

import pytest
from ruamel import yaml


@pytest.fixture
def message():
    """Return message for testing."""
    return {'from': 'harry s truman', 'text': 'the buck stops here'}


@pytest.fixture
def messages():
    """Return all messages for testing."""
    yml = yaml.YAML(typ='safe', pure='True')
    return_messages = yml.load(open('tests/compliments.yml'))
    return return_messages
