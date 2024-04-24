from twisted.internet import protocol, reactor

class StarServer(protocol.Protocol):
    def __init__(self):
        self.clients = set()

    def connectionMade(self):
        # Add this client to the set of clients
        self.clients.add(self)

    def dataReceived(self, data):
        # Send the data to all clients except the sender
        for client in self.clients:
            if client is not self:
                client.transport.write(data)

    def connectionLost(self, reason):
        # Remove this client from the set of clients
        self.clients.remove(self)

class StarServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return StarServer()

reactor.listenTCP(8000, StarServerFactory())
reactor.run()