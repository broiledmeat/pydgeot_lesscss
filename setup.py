#!/usr/bin/env python3
from distutils.core import setup


setup(
    name='pydgeot_lesscss',
    description='LessCSS support for Pydgeot.',
    url='https://github.com/broiledmeat/pydgeot_lesscss',
    license='Apache License, Version 2.0',
    author='Derrick Staples',
    author_email='broiledmeat@gmail.com',
    version='0.2',
    packages=['pydgeot.plugins.lesscss'],
    requires=['pydgeot', 'lesscpy'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup'
    ]
)
