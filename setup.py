#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

PROJECT = 'osbapi'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = 'Command line tool to work with OSBAPI'

setup(
    name=PROJECT,
    version=VERSION,

    description='OSBAPI command line tool ',
    long_description=long_description,

    author='Narasimha SV',

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'osbapi = osbapicli.main:main'
        ],
        'osbapi': [
            'catalog = osbapicli.simple:Catalog',
            'provision = osbapicli.simple:Provision',
            'deprovision = osbapicli.simple:DeProvision',
        ],
    },

    zip_safe=False,
)
