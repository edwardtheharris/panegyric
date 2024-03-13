---
abstract: Usage information for Panegyric.
authors: Xander Harris
date: 2024-03-12
title: Usage
---

## Installation

1. Make sure you've got Python 3 installed with `pipenv`{l=shell} available.

    ```{code-block} shell
    pip3 install -U pip pipenv
    ```

2. Then use pipenv to install the required dependencies and
   enter the created virtualenv.

    ```{code-block} shell
    pipenv install --dev
    pipenv shell
    ```

3. From this virtualenv you can build and install the package.

    ```{code-block} shell
    python setup.py build
    python setup.py install
    ```

### Install with pip

Or you can use pip to install the package locally.

```{code-block} shell
pip install -e .
```

## Execution

At the moment there are no arguments, so changing
things like the phone number to text and enabling
non-test executions require updating the `src/panegyric/text.py`
source file directly.

Eventually there will be a config file or something to make
this kind of thing easier, but for now this will work.

Once you've got the package installed and the `Text` class
configured you can run the program.

```{code-block} shell
panegyric
```

At the time of writing this is meant to be executed once
a day via a cron job or similar timed program execution
tool.
