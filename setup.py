# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in zytoenergese/__init__.py
from zytoenergese import __version__ as version

setup(
	name='zytoenergese',
	version=version,
	description='ERPNext Apps',
	author='libracore AG',
	author_email='info@libracore.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
