from twisted.internet import protocol, reactor

class Mesh(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.peers = set()

    def connectionMade(self):
        # Add this client to the set of peers for all other clients
        for peer in self.factory.clients:
            if peer is not self:
                peer.peers.add(self)
                self.peers.add(peer)
                peer.transport.write(f"CONNECT {self.transport.getPeer().host}\r\n".encode())
        self.factory.clients.add(self)

    def dataReceived(self, data):
        # Send the data to all peers
        for peer in self.peers:
            peer.transport.write(data)

    def connectionLost(self, reason):
        # Remove this client from the set of peers for all other clients
        for peer in self.peers:
            peer.peers.remove(self)
            peer.transport.write(f"DISCONNECT {self.transport.getPeer().host}\r\n".encode())
        self.factory.clients.remove(self)

class MeshFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        protocol = Mesh(self)
        return protocol

reactor.listenTCP(8000, MeshFactory())
reactor.run()