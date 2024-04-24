from twisted.internet import protocol, reactor

class Ring(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.next = None

    def connectionMade(self):
        # Get the list of all clients in the ring
        clients = list(self.factory.clients)
        # Find the index of this client in the list
        index = clients.index(self)
        # Set the "next" client to the client with the next index
        self.next = clients[(index + 1) % len(clients)]

    def dataReceived(self, data):
        # Forward the data to the next client in the ring
        self.next.transport.write(data)

class RingFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        protocol = Ring(self)
        self.clients.add(protocol)
        return protocol

reactor.listenTCP(8000, RingFactory())
reactor.run()
