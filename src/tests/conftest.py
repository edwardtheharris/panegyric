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


@pytest.fixture
def api_response():
    """Return a mocked API reponse."""
    return {
        '_content': (b'{ "success": false,'
                     b' "error": "Out of quota",'
                     b' "quotaRemaining": 0}'),
        '_content_consumed': True,
        '_next': None,
        'connection': ('< requests.adapters.HTTPAdapter'
                       ' object at 0x105860070 > '),
        'cookies': '< RequestsCookieJar[] > ',
        'elapsed': 'datetime.timedelta(microseconds=206048)',
        'encoding': 'utf-8',
        'headers': {
            'Date': 'Tue, 03 Aug 2021 20:55:37 GMT',
            'Content-Type': 'application/json; charset=utf-8',
            'Transfer-Encoding': 'chunked',
            'Connection': 'keep-alive',
            'CF-Ray': '679272a8ab8731a9-LAX',
            'Access-Control-Allow-Origin': '*',
            'ETag': 'W/"3b-fOPG0i2Yi6s4n2M0ob5s5I1zxew"',
            'CF-Cache-Status': 'DYNAMIC',
            'Expect-CT': ('max-age=604800, '
                          'report-uri="https://report-uri.cloudflare.com/'
                          'cdn-cgi/beacon/expect-ct"'),
            'X-Powered-By': 'Express',
            'X-textbelt-proxied': '1',
            'Report-To': ('{"endpoints":[{"url":"https:\\/\\/a.'
                          'nel.cloudflare.com\\/report\\/v3?s=Z'
                          't6UnKAUpEEKgkjnT%2FIE9cZQDA7J3UrZcx9'
                          'v7f7CmZYsaD46FeWHddrddcgrfEmZmKozp8H'
                          'keqiiq%2FtUVba4g3%2BP7I3MQN3bUzAGJOy'
                          'YLeSacBfCD%2BoOFAtoH1nmlN4opR6S%2B6n'
                          'tcx1grBQ%3D"}],"group":"cf-nel","max_age":604800}'),
            'NEL': '{"report_to":"cf-nel","max_age":604800}',
            'Vary': 'Accept-Encoding',
            'Server': 'cloudflare',
            'Content-Encoding': 'gzip',
            'alt-svc': ('h3-27=":443"; ma=86400, h3-28=":443"; ma=86400,'
                        ' h3-29=":443"; ma=86400, h3=":443"; ma=86400')},
        'history': [],
        'raw': '< urllib3.response.HTTPResponse object at 0x105808af0 > ',
        'reason': 'OK',
        'request': '< PreparedRequest [POST] > ',
        'status_code': 200,
        'url': 'https://textbelt.com/text'}
