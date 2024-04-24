from twisted.internet import protocol, reactor

class Bus(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.clients = set()

    def connectionMade(self):
        self.factory.clients.add(self)

    def dataReceived(self, data):
        for client in self.factory.clients:
            if client != self:
                client.transport.write(data)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

class BusFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return Bus(self)

reactor.listenTCP(8000, BusFactory())
reactor.run()
