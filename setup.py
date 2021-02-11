#!/usr/bin/env python

"""Setup script for the datetoolz module distribution."""

from setuptools import setup
import io
import sys
# from datetoolz import __version__ as datetoolz_version
__version__ == "alpha"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='datetoolz',
    version=__version__,
    description='Simplify working with dates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Amit Kothiyal',
    author_email='kothiyal.tima@gmail.com',
    url='https://github.com/tima04/datetoolz',
    download_url='https://github.com/tima04/datetoolz',
    license='MIT License',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='python datetime lubridate', 
    install_requires=['pyparsing'],
    python_requires='>=3.6'
)
