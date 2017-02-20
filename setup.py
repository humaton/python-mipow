#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = 0.3

setup(
    name='mipow_comet',
    version=0.3,
    author='Andreas Hohler',
    author_email='east7074@gmail.com',
    url='https://github.com/papagei9/python-mipow',
    packages=find_packages(),
    download_url='https://github.com/papagei9/python-mipow/tarball/0.3',
    scripts=[],
    description='Python API for controlling Mipow COMET LED stripes',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
