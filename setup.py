#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='Text My Wife',
    description='Automation for complimenting my wife.',
    author='Edward Harris',
    author_email='plebis@hotmail.com',
    entry_points={
        "console_scripts": "textmywife=textmywife.text:main",
    },
    install_requires=[
        'python-dotenv',
        'requests',
        'ruamel.yaml'
    ],
    packages=setuptools.find_packages(),
    version='v0.1.0',
)
