#!/usr/bin/python
# -*- coding: utf-8 -*-

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup
setup(
    name='pikaboo',
    version='0.1.0',
    author='codemaniac',
    author_email='ashish.ap.rao@gmail.com',
    packages=['pikaboo'],
    scripts=['bin/pikaboo'],
    url='https://github.com/codemaniac/pikaboo',
    license='BSD',
    description='Library and CLI to perform steganography',
    long_description=open('README.md').read(),
    keywords = 'steganography PIL',
    install_requires=['setuptools','pil','argparse'],
)
