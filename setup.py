#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from codecs import open as fopen
from os.path import dirname, abspath, join
from setuptools import setup, find_packages

VERSION = "0.1.0"

DIR = dirname(abspath(__file__))

with fopen(join(DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'faker_scifi',
    version = VERSION,
    description = 'Faker provider for science fiction gobbledygook.',
    long_description = long_description,
    license = 'MIT',
    keywords = 'faker faker-library faker-provider faker-generator scifi',
    author = 'Garison Spaeth',
    author_email = 'greesha@gmail.com',
    url = 'https://github.com/scummchild/faker_scifi',
    download_url = 'https://github.com/scummchild/faker_scifi/archive/v{0}.zip'.format(VERSION),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    packages = find_packages(exclude=['docs', 'tests', 'tests.*']),
    test_suite = 'test',
    install_requires = [
        'Faker',
    ],
)
