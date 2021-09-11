# panegyric

[![circle ci build status](https://circleci.com/gh/edwardtheharris/panegyric.svg?style=shield)](https://app.circleci.com/pipelines/github/edwardtheharris/panegyric) [![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com) [![codecov](https://codecov.io/gh/edwardtheharris/panegyric/branch/main/graph/badge.svg?token=7D17IAT6L7)](https://codecov.io/gh/edwardtheharris/panegyric)

A tool for sending praise via text on a regular schedule.

## Usage

Make sure you've got Python 3 installed with pipenv available.

```bash
pip3 install pipenv
```

Then use pipenv to install the required dependencies and
enter the created virtualenv.

```bash
pipenv install --dev
pipenv shell
```

### Build and install with python

From this virtualenv you can build and install the package.

```bash
python setup.py build
python setup.py install
```

### Install with pip

Or you can use pip to install the package locally.

```bash
pip install -e .
```

### Execution

At the moment there are no arguments, so changing
things like the phone number to text and enabling
non-test executions require updating the `src/panegyric/text.py`
source file directly.

Eventually there will be a config file or something to make
this kind of thing easier, but for now this will work.

Once you've got the package installed and the `Text` class
configured you can run the program.

```bash
panegyric
```

At the time of writing this is meant to be executed once
a day via a cron job or similar timed program execution
tool.

## Testing

Tests are run with [pytest](https://docs.pytest.org/en/6.2.x/).

```bash
pytest -s -v -l
```

## Documentation

You can build the docuentation with Sphinx.

```bash
sphinx-build docs/source docs/build
```
