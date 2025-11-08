from setuptools import setup, find_packages
from typing import List

setup(
    name='LiveSensor',
    version='0.0.1',
    author='Shivang',
    author_email='shiva@gmail.com',
    packages=find_packages(),
    install_requires=['pymongo']
)