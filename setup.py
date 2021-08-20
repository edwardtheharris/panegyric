#!/usr/bin/env python3
"""Setup tools configuration."""

import setuptools

setuptools.setup(
    name='Panegyric',
    description='Automated compliments via text',
    author='Xander Harris',
    author_email='xandertheharris@gmail.com',
    entry_points={
        "console_scripts": "panegyric=panegyric.text:main",
    },
    install_requires=[
        'requests',
        'ruamel.yaml'
    ],
    packages=setuptools.find_packages(),
    version='v0.1.0',
)
