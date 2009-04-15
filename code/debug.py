"""
debug.py
"""

from logging import getLogger
from logging import StreamHandler
from logging import FileHandler
from logging import INFO
from logging import DEBUG
from logging import Formatter
from sys import stderr
from os.path import join

from platforms import get_config_dir

#log.critical("Critical = 50")
#log.error("Error = 40")
#log.warning("Warning = 30")
#log.info("Info = 20")
#log.debug("Debug = 10")

log_name = "debug"

def get_log():
	"""
	Returns the debug log. Really needs some work in refactoring;
	but first we need a decent architecture for this.
	"""
	debug_log = getLogger(log_name)
	if debug_log.handlers == []:
		config_dir = get_config_dir()
		log_file = join(config_dir, log_name)
	
		file_format = "%(levelname)s - %(filename)s, line %(lineno)s: %(message)s"
		formatter = Formatter(file_format)
	
		file_log = FileHandler(log_file)
		file_log.setFormatter(formatter)
	
		debug_log.addHandler(StreamHandler(stderr))
		debug_log.addHandler(file_log)

		debug_log.setLevel(-1)
		done = True
	return debug_log

def set_level(level):
	logger = get_log()
	logger.setLevel(level)

# vim:ts=4:sw=4:tw=72:fdm=indent
