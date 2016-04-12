#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='YourAppName',
    # GETTING-STARTED: set your app version:
    version='2.0',
    # GETTING-STARTED: set your app description:
    description='InnovaMex App Django',
    # GETTING-STARTED: set author name (your name):
    author='Your Name',
    # GETTING-STARTED: set author email (your email):
    author_email='email@email.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.9.5',
        'whitenoise==3.0',
        'brotlipy==0.2.0'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
