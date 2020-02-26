"""
The setup script used if API needs to be used as a package/library
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

config = {
    'description': 'Sample API for the iris dataset',
    'author': 'Vasileios Papapanagiotou',
    'url': '',
    'author_email': 'bpapapana@gmail.com',
    'version': '1.0',
    'install_requires': required,
    'packages': ['iris_api'],
    'name': 'iris_api'
}

setup(**config)
