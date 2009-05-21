#!/usr/bin/env python
"""Synchronization of two directories using rsync

Code released under a free software compatible license. See LICENSE for
more details.
Original author: Chad Wollenberg
Code patches by:
        Nido Media

"""

from subprocess import call
from sys import stderr
from sys import exit

# Set path to rsync command
rsync = "rsync"


def main():
    source = raw_input ("Please enter source directory: ")
    target = raw_input ("Please enter destination directory: ")
    exit_value = sync(source, target)
    exit(exit_value)


def echo(cmd):
    """
    Echo and execute command called via subprocess.call
    """
    print cmd
    ret = call (cmd, shell=True)
    return ret


def sync(source, target):
    arguments = "-a"
    cmd = "%s %s %s %s" % (rsync, arguments, source, target)
    return echo(cmd)
    
def delete(source, target):
    arguments = "-a --delete"
    cmd = "%s %s %s %s" % (rsync, arguments, source, target)
    return echo(cmd)
 

if __name__ == "__main__":
    main()

# vim:ts=4:sw=4:tw=72:fdm=indent:expandtab
