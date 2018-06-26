#!/usr/bin/env python
from setuptools import setup,find_packages

setup(name='elliptic-curves',
      version=0.1.0,
      description='Elliptic Curve',
      author='Adam Buran',
      author_email='aburan28@gmail.com',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      test_suite='nose.collector', tests_require=['nose', 'pytest', 'cython'],
      package_data={'': ['*.md', '*.rst']}
)

