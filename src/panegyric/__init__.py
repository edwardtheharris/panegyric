#!/usr/bin/env python3
"""The main panegyric package."""

import sentry_sdk
sentry_sdk.init(
    ("https://a40e278a662e46db86ef8aa4d7a46fbd@o325200"
     ".ingest.sentry.io/5955114"),

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
