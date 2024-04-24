"""The most basic chat protocol possible.

to run:
Terminal 1: twistd -y chatserver.py(filename) and press enter
Terminal 2: telnet localhost 1025 and press enter then tye any msg
Terminal 3: telnet localhost 1025 and press enter and type any msg
"""
from __future__ import print_function

from twisted.protocols import basic



class MyChat(basic.LineReceiver):
    def connectionMade(self):
        print("Got new client!")
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print("Lost a client!")
        self.factory.clients.remove(self)

    def lineReceived(self, line):
        print("received", repr(line))
        for c in self.factory.clients:
            c.message(line)

    def message(self, message):
        self.transport.write(message + b'\n')


from twisted.internet import protocol
from twisted.application import service, internet

factory = protocol.ServerFactory()
factory.protocol = MyChat
factory.clients = []

application = service.Application("chatserver")
internet.TCPServer(1025, factory).setServiceParent(application)