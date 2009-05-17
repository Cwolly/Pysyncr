#!/usr/bin/env python
"""Opens port 6060 to listen for an incoming connection from clients

Code released under a free software compatible license. See LICENSE for
more details.
Original author: Chad Wollenberg
Code patches by:
        

"""

from twisted.internet import reactor, protocol
from twisted.protocols import basic

class EchoProtocol(basic.LineReceiver):
    def lineReceived(self, line):
        if line == 'quit':
            self.sendLine("Terminating Server")
            self.transport.loseConnection( )
        else:
            self.sendLine("Server Awaiting Connections")

if __name__ == "_ _main_ _":
    port = 6060
    reactor.listenTCP(port, )
    reactor.run( )

