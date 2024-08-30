"""Metadata related to the panegyric project."""
# SPDX-FileCopyrightText: 2024-present Xander Harris <xandertheharris@gmail.com>
#
# SPDX-License-Identifier: MIT
from pathlib import Path

import version_query

def get_version():
    """Return the most recent version of the project."""
    try:
        ret_value = version_query.query_folder(Path('.'))
    except ValueError:
        ret_value = version_query.Version.from_str('0.0.1')
    return ret_value

__version__ = get_version()
