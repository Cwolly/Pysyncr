""" Configuration file for inotifysample.py
Code released under a free software compatible license. See LICENSE for
more details.
Original author: James Polera
Code patches by:

"""


DEBUG = True

# Create WATCH and DESTINATION dirs
CREATE_DIRS = False

# Directory to watch
# TODO:  Make this multi-directory capable 
#         SQLite for configuration storage?
WATCH = '/home/james/tmp/'

# Directory to sync with
DESTINATION = '/home/james/dest/'

if CREATE_DIRS:
    from os import path, makedirs
    
    # Create WATCH directory if it doesn't exist
    if not path.exists(WATCH):
        makedirs(WATCH)
        
    # Create DESTINATION directory if it doesn't exist
    if not path.exists(DESTINATION):
        makedirs(DESTINATION)
    
