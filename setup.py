#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import io
import os
import re

setup_path = os.path.abspath(__file__)
setup_path_dir = os.path.dirname(setup_path)

exec(open(os.path.join(setup_path_dir, 'pyarchive', 'version.py')).read())

long_description = "coarse tool to move targets to a type specific location"

setup(
    name='pyarchive',
    version=__version__,
    description=long_description,
    keywords='pyarchive',
    install_requires=['click>=6.7,<7.0'],
    long_description=long_description,
    author='John van Zantvoort',
    author_email='john@vanzantvoort.org',
    url='https://github.com/jvzantvoort/pyarchive',
    packages=find_packages(exclude=['docs', 'docs-src', 'tests']),
    license='MIT',
    test_suite="tests",
    entry_points='''
      [console_scripts]
      pyarch=pyarchive.cli:cli
    ''',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Office/Business',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
    ]
)
