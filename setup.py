# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='spotlight',
    version='0.0.1',
    description='Spotlight is a cli framework for python',
    long_description=readme,
    author='Sachin Kumbhojkar',
    author_email='sachin755@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

