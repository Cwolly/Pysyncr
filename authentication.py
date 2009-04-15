#!/usr/bin/env python
""" Initial creation of a username and password. This eventually will need to be hashed somehow, and the password will need to be saved on the server somehow """

import sys
import paramiko #paramiko implements the python ssh library
from twisted.internet import reactor, defer, protocol

hostname = raw_input ("Please enter the IP or hostname of the pysyncr server: ") #needs to be stored for ssh and rsync connection later
port = raw_input ("Please enter the port that the server uses to connect (default is 22):")
username = raw_input ("Please create a username: ") #needs to be stored as permanent user authentication on server
userpass = raw_input ("Please create a password: ") #needs to be stored as permanent user password on server


"""not complete, this section will check to see if the given hostname and port will connect client to server"""

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
