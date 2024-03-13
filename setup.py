#!/usr/bin/env python3
"""Setup tools configuration."""
# pylint: disable=E0401
import pathlib
import setuptools

def get_version():
    """Get the project's version."""
    vpath = pathlib.Path('version')
    with vpath.open('r', encoding='utf-8') as v_fh:
        version = v_fh.read()
    return version

with pathlib.Path('readme.md').open("r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    author='Xander Harris',
    author_email='xandertheharris@gmail.com',
    description='Automated compliments via text',
    entry_points={
        "console_scripts": "panegyric=panegyric.text:main",
    },
    install_requires=[
        'requests',
        'ruamel.yaml',
        'sentry-sdk',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    name='Panegyric',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    project_urls={
        "Bug Tracker": "https://github.com/edwardtheharris/panegyric/issues",
    },
    url="https://github.com/edwardtheharris/panegyric",
    version=get_version(),
)
