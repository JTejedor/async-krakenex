#!/usr/bin/env python3

import os.path
from distutils.core import setup

exec(open('./asynckrakenex/version.py').read())


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='asynckrakenex',
      version=__version__,
      description='async kraken.com cryptocurrency exchange API',
      long_description=read('README.rst'),
      author='Noel Maersk, Jesus Tejedor',
      author_email='veox+packages+spamremove@veox.pw',
      url=__url__,
      install_requires=[
          'aiohttp>=2.2.0'
      ],
      packages=['asynckrakenex'],
      python_requires='>=3.3',
      classifiers=[
          'Programming Language :: Python :: 3.6',
      ],
      )
