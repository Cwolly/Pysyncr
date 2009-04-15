"""
platforms takes care of platform related stuff

Supports the configuration of different platforms around. Development is
done on Linux. There has been some problems on windows. This version
should work on anything around.

Code released under a free software compatible license. See LICENSE for
more details.
Original author: Nido Media
Code patches by:
	David Abbott 
"""

from os import name
from os import getenv
from os.path import join
from os.path import exists
from sys import stderr
from os import makedirs

program_name = 'pysyncr'

# os.name an be posix, nt, dos and mac
home = getenv("HOME")
drive = getenv("HOMEDRIVE")
path = getenv("HOMEPATH")
profile = getenv("USERPROFILE")

def get_base_dir():
	"""
	By default, the base_dir is the current directory. But most
	platforms have a certain place where configuration directories
	belong. This function gets the specific configuration directory
	if possible, or returns the current directory instead.
	"""
	base_dir = "."

	if name == 'posix':
		base_dir = home

	elif name == 'nt':
		if drive and path:
			base_dir = join(drive, path)
		elif profile:
			base_dir = profile
		elif home:
			base_dir = home

	elif name == "dos":
		# "." seems the best idea
		pass

	elif name == "mac":
		# I remember this from OS-X
		if home:
			base_dir = home
	
	return base_dir

def get_config_dir():
	"""
	The configuration directory as described by how certain
	platforms want them.
	"""
	base = get_base_dir()
	
	# default to UNIX style hidden directories.
	path = '.' + program_name

	if (name is 'nt') or (name is 'dos'):
		# Microsoft disagrees
		path = program_name

	config_dir = join(base, path)
	if not exists(config_dir):
		makedirs(config_dir)
	return config_dir

# vim:ts=4:sw=4:tw=72:fdm=indent
