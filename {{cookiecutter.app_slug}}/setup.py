#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


setup(
    author="{{cookiecutter.author_name}}",
    author_email='{{cookiecutter.author_email}}',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Cli to manage your django project",
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{cookiecutter.app_slug}}',
    name='{{cookiecutter.app_slug}}',
    packages=find_packages(include=['{{cookiecutter.app_slug}}', '{{cookiecutter.app_slug}}.*']),
    test_suite='tests',
    version='0.1.0',
    zip_safe=False,
)
