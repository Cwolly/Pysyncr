#!/usr/bin/env python
#synchronization of two directories via rsync

from subprocess import call
import sys

source = raw_input ("Please enter source directory: ")
target = raw_input ("Please enter destination directory: ")
rsync = "rsync"
arguments = "-a"
cmd = "%s %s %s %s" % (rsync, arguments, source, target)

def sync():

    ret = call (cmd, shell=True)
    if ret !=0:
        print "rsync failed"
        sys.exit(1)
sync()
