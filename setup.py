#!/usr/bin/env python

from setuptools import setup

setup(name='pandohs',
      packages=['pandohs'],
      version='0.01',
      description='Pandohs Data Validation',
      author='Kallin Nagelberg',
      author_email='kallin.nagelberg@gmail.com',
      url='https://github.com/Kallin/pandohs',
      install_requires=['pandas'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
      )
