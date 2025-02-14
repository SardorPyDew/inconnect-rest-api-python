from setuptools import setup, find_packages
from sys import version_info
from Inconnect import (
    __author__,
    __author_email__,
    __version__
)

install_requires = ['python3-memcached', 'requests', 'deprecated']

if version_info.major == 2:
    install_requires = ['python-memcached', 'requests', 'simplejson']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="inconnect",
    version=__version__,
    packages=find_packages(),
    
    author=__author__,
    author_email=__author_email__,
    description='A simple Inconnect REST client library and example for Python',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/radiants-uz/inconnect-rest-api-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires
)