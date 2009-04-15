"""
This class takes care of most file related tasks. Exception of this is
the download_log, which in a class and file of it's own.

Code released under a free software compatible license. See LICENSE for
more details.
Original author: Nido Media
Code patches by:
	...
"""

from os.path import isdir
from os.path import isfile
from os.path import exists
from os.path import join
from os.path import dirname
from os import makedirs

from debug import get_log

logger = get_log()



def prepare_directory(directory):
	"""
	Checks if a directory is available and creates it, and it's
	parent directories, if necessary.
	"""
	if not exists(directory):
		logger.info('Directory ' + directory +
			' does not exist. Creating it.')
		makedirs(directory)
	if not isdir:
		logger.critical(directory + 'is not a directory. Exiting.')
		exit(1)

def prepare_file(filename):
	"""
	Checks if filename exists and creates it if necessary.
	If it is not a file, it will exit the program.
	False.
	"""
	if not exists(filename):
			logger.info('file ' + filename + 
					' does not exist.  Creating it.')
			file(filename, "w").close()
	if not isfile(filename):
		logger.critical(filename + ' is not a file. Exiting.')
		exit(1)

# vim:ts=4:sw=4:tw=72:fdm=indent
