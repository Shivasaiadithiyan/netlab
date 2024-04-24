from twisted.internet import ssl, reactor
from twisted.internet.protocol import Protocol, ClientFactory

class EchoClient(Protocol):
    def connectionMade(self):
        self.transport.write("Hello, world!")

    def dataReceived(self, data):
        print ("Server said:", data)
        self.transport.loseConnection()

class EchoClientFactory(ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print ("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print ("Connection lost.")
        reactor.stop()

contextFactory = ssl.ClientContextFactory()
reactor.connectSSL('localhost', 8000, EchoClientFactory(), contextFactory)
reactor.run()
