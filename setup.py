#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (3, 6):
    sys.exit(
        'Python < 3.6 is not supported. You are using Python {}.{}.'.format(
            sys.version_info[0], sys.version_info[1])
    )

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('requirements.txt', 'r') as f:
    required_packages = f.read().splitlines()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://python_claml.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='python_claml',
    version='0.1.0',
    description='A ClaML reader for Python.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Gijs Kant',
    author_email='gijs@thehyve.nl',
    url='https://github.com/thehyve/python_claml',
    packages=[
        'python_claml',
    ],
    package_dir={'python_claml': 'python_claml'},
    include_package_data=True,
    python_requires='>=3.6.0',
    install_requires=required_packages,
    license='MIT',
    zip_safe=False,
    keywords='python_claml',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='tests',
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle'
    ]
)
