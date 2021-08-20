#!/usr/bin/env python3
"""Setup tools configuration."""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    author='Xander Harris',
    author_email='xandertheharris@gmail.com',
    description='Automated compliments via text',
    entry_points={
        "console_scripts": "panegyric=panegyric.text:main",
    },
    install_requires=[
        'python-dotenv',
        'requests',
        'ruamel.yaml'
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
    version='v0.1.0',
)
