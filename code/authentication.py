#!/usr/bin/env python
"""Initial creation of a user name and password.

This eventually will need to be hashed somehow, and the password will
need to be saved on the server somehow.

This is not yet complete, this section will check to see if the given
host name and port will connect client to server

Code released under a free software compatible license. See LICENSE for
more details.
Original author: Chad Wollenberg
Code patches by:
    Nido Media

"""

import sys
import paramiko #paramiko implements ssh 2
from twisted.internet import reactor, defer, protocol
from download_log import access_log

def main():
    configure()

def configure():
    """ Configures the system according to the configuration file.

    Takes raw_input if no default configuration is known. (This should
    change).

    """
    config = access_log("configuration")
    host = config.has('host')
    if not host:
        host = raw_input ("Please enter the IP or host name of the pysyncr server: ") #needs to be stored for ssh and rsync connection later
        config.add('host', host)
    
    port = config.has('host')
    if not port:
        port = raw_input ("Please enter the port that the server uses to connect (default is 22):")
        config.add('port', port)

    user = config.has('user')
    if not user:
        user = raw_input ("Please create a username: ") #needs to be stored as permanent user authentication on server
        config.add('user', user)

    password = config.has('password')
    if not password:
        password = raw_input ("Please create a password: ") #needs to be stored as permanent user password on server
        config.add('password', password)


class CallbackAndDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.deferred.callback("Connected!")
        self.transport.loseConnection( )

class ConnectionTestFactory(protocol.ClientFactory):
    protocol = CallbackAndDisconnectProtocol

    def __init__(self):
        self.deferred = defer.Deferred( )

    def clientConnectionFailed(self, connector, reason):
        self.deferred.errback(reason)

def testConnect(hostname, port):
    testFactory = ConnectionTestFactory( )
    reactor.connectTCP(host, port, testFactory)
    return testFactory.deferred

def handleSuccess(result, port):
    pass

if __name__ == "__main__":
    main()
