"""
A "download_log" is a sort of log which keeps track of strings without
newlines in them. In it's first use, this string was an URL log; keeping
track of what files have been downloaded.

Apart from keeping a dictionary while the program is running; it also
keeps track of a file in the 'config path' in the configuration module.

While theoretically everything could be put in, the saving algorithm
(and file definition) only allows text files.

NOTE: This is not thread safe. You could save two different instances of
a log and get a problem because both threads will write to disk!

Code released under a free software compatible license. See LICENSE for more
details.
Original author: Nido Media
Code patches by:
	...
"""

from os.path import join
from re import compile

from files import prepare_directory
from files import prepare_file
from debug import get_log
from platforms import get_config_dir

logger = get_log()


def access_log(name, directory=get_config_dir()):
	"""
	Opens log 'name'. Returns a download_log with the given name.
	The logs are matched to a file which is updated as well.
	"""
	if name in download_log.open_logs:
		result = download_log.open_logs[name]
	else:
		logger.debug("Log " + name + " not yet open, opening.")
		result = download_log(name, directory)
	return result

class download_log:
	"""
	A download log is a log which is linked to a file on disk. This
	log can be added to, or searched whether a key is present or
	not.
	"""
	open_logs = {}

	def __init__(self, filename, directory):
		download_log.open_logs[filename] = self
		configurer = compile(r'(?P<key>[^ ]*)\s*=\s*(?P<value>[^ ]*)')
		self.__log_file__ = join(directory, filename)
		self.__dictionary__ = {}

		prepare_directory(directory)
		prepare_file(join(self.__log_file__))

		open_file = file(self.__log_file__)
		log_string = open_file.read()
		split_string = log_string.split("\n")
		for line in split_string:
			key = line
			value = None
			match = configurer.match(line)
			if match:
				key = match.group("key")
				value = match.group("value")
			self.__dictionary__[key] = value

	def add(self, key, value=None):
		"""
		Adds the key to the log. Also saves the result to the
		log file.

		TODO: This function now saves certain keys double if they change
		over time (or added superfluously). This should be fixed here
		(or at least be considered while changing the file);
		alternatively, a function to clean could be added and executed
		manually.
		"""
		self.__dictionary__[key] = value

		log = file(self.__log_file__, "a")

		string = key
		if value:
			string = key + " = " + value
		string = string + "\n"

		log.write(string)
		log.close()

	def add_temporarily(self, key, value=None):
		"""
		Adds the key to the log; but does not save the result in the log
		file. The adding of this key is thus forgotten when the program
		is restarted.
		
		TODO: Please notice this functionality opposes to the reason
		this class was created. Also; there's no notice of the temporal
		status in this class in case a clean up function was to be
		created.
		TODO: there's some problems with using multiple files.
		"""
		self.__dictionary__[key] = value

	def has(self, key):
		"""
		Determines if a key is available in the log. Returning
		True or False according to the case.
		"""
		result = False
		if key in self.__dictionary__:
			result = True
			if self.__dictionary__[key] != None:
				result = self.__dictionary__[key]
		return result

	def get_filename(self):
		"""
		Returns the path of the file on disk.
		"""
		return self.__log_file__

# vim:ts=4:sw=4:tw=72:fdm=indent
