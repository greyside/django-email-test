#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import django_email_test

setup(name='django-email-test',
	version=django_email_test.__version__,
	description="An app for sending test emails via the admin site to make sure your email server is working.",
	author='Seán Hayes',
	author_email='sean@seanhayes.name',
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Framework :: Django",
		"Intended Audience :: Developers",
		"Intended Audience :: System Administrators",
		"License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.6",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Internet :: WWW/HTTP :: Site Management",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
	],
	keywords='django admin email test',
	url='https://github.com/SeanHayes/django-email-test',
	license='BSD',
	packages=['django_email_test'],
	install_requires=['Django>=1.2',],
)

