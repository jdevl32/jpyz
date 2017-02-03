#!/usr/bin/env python3
# setup.py

"""
...
"""

from setuptools import setup, find_packages

_NAME = "jpyz"

setup(
    name=_NAME
    ,
    version="0.1.0+2017.01.11.0023"
    ,
    packages=find_packages\
        (
            exclude=
            [
                "test"
            ]
        )
    ,
    install_requires=
    [
        'pexpect'
    ]
)
