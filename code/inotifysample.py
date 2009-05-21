#!/usr/bin/env python
"""Use of the pyinotify library

This code is pretty much ripped off the pyinotify website
(http://pyinotify.sourceforge.net/) with some minor changes.
Should give us a good basis for our client (at least on Linux
systems)

I'd like to make this multi-threaded at some point, but for 
now it should serve as a proof of concept.


Code released under a free software compatible license. See LICENSE for
more details.
Original author: James Polera
Code patches by:

"""

# Dependencies
"""
Hey, this script has some dependencies:
  - pyinotify
      on Debian systems:
        apt-get install python-pyinotify
"""

import os
from pyinotify import WatchManager, Notifier, ThreadedNotifier, \
                      EventsCodes, ProcessEvent
import inotify_config
from rsyncwrap import sync, delete

DEBUG = inotify_config.DEBUG

wm = WatchManager()

mask = EventsCodes.IN_DELETE | EventsCodes.IN_CREATE  # watched events

class PTmp(ProcessEvent):
    def process_IN_CREATE(self, event):
        new_file = os.path.join(event.path, event.name)
        print "Create: %s" %  new_file
        sync(inotify_config.WATCH, inotify_config.DESTINATION)

    def process_IN_DELETE(self, event):
        new_file = os.path.join(event.path, event.name)
        print "Remove: %s" %  new_file
        delete(inotify_config.WATCH, inotify_config.DESTINATION)

if __name__ == "__main__":
    if DEBUG:
        print "Watching %s for changes..." % inotify_config.WATCH
    notifier = Notifier(wm, PTmp())
    wdd = wm.add_watch('%s' % inotify_config.WATCH, mask, rec=True)
    while True:  # loop forever
        try:
            # process the queue of events as explained above
            notifier.process_events()
            if notifier.check_events():
                # read notified events and enqeue them
                notifier.read_events()
            # you can do some tasks here...
        except KeyboardInterrupt:
            # destroy the inotify's instance on this interrupt 
            # (stop monitoring)
            notifier.stop()
            break

