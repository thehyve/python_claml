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

with open('requirements.txt', 'r') as f:
    required_packages = f.read().splitlines()

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit fhir2transmart/__version__.py
version = {}
with open(os.path.join(here, 'python_claml', '__version__.py')) as f:
    exec(f.read(), version)

readme = open('README.rst').read()

setup(
    name='python_claml',
    version=version['__version__'],
    description='A ClaML reader for Python.',
    long_description=readme + '\n\n',
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
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark',
        # dependency for `python setup.py bdist_wheel`
        'wheel'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle'
    ]
)
