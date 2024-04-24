from twisted.internet import reactor, protocol

class StarProtocol(protocol.Protocol):
    def __init__(self):
        self.peer_name = None

    def connectionMade(self):
        self.peer_name = self.transport.getPeer().host
        print("New device connected: {}".format(self.peer_name))

    def dataReceived(self, data):
        print("Received data from {}: {}".format(self.peer_name, data.decode()))
        self.transport.write("ACK".encode())

class StarFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return StarProtocol()

if __name__ == '__main__':
    factory = StarFactory()
    reactor.listenTCP(8000, factory)
    reactor.run()

