import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Minuteman",
    version = "0.0.1",
    author = "David Lance",
    author_email = "david6116@yahoo.com",
    description = "Multi-user time tracking application written in django.",
    packages = ['minuteman'],
    long_description = read('README'),
    classifiers = [
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
    ],
)
