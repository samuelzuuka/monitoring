#!/usr/bin/env python
# Encoding: utf-8
# See: <http://docs.python.org/distutils/introduction.html>
from distutils.core import setup
import os, sys
VERSION = eval(filter(lambda _:_.startswith("__version__"), file("Sources/watchdog.py").readlines())[0].split("=")[1])
setup(
	name             = "watchdog",
	version          = VERSION,
	description      = "Server monitoring and data-collection daemon",
	author           = "Sébastien Pierre",
	author_email     = "sebastien.pierre@gmail.com",
	url              = "http://github.com/sebastien/watchdog",
	download_url     = "https://github.com/sebastien/watchdog/tarball/%s" % (VERSION),
	keywords         = ["daemon", "services", "monitoring", "administration"],
	install_requires = [],
	package_dir      = {"":"Sources"},
	py_modules       = ["watchdog"],
	scripts          = ["Scripts/watchdog"],
	classifiers      = [
		"Programming Language :: Python",
		"Development Status :: 3 - Alpha",
		"Natural Language :: English",
		"Environment :: Web Environment",
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Topic :: Utilities"
	],
)
# EOF - vim: ts=4 sw=4 noet
