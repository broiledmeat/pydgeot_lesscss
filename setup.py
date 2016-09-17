#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='pydgeot_lesscss',
    version='0.1',
    packages=['pydgeot.plugins.lesscss'],
    requires=['pydgeot', 'lesscpy'],
    url='https://github.com/broiledmeat/pydgeot_lesscss',
    license='Apache License, Version 2.0',
    author='Derrick Staples',
    author_email='broiledmeat@gmail.com',
    description='LessCSS support for Pydgeot.'
)
