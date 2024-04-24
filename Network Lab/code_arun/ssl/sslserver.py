from twisted.internet import ssl, reactor
from twisted.internet.protocol import Protocol, Factory

class Echo(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(Factory):
    def buildProtocol(self, addr):
        return Echo()

factory = EchoFactory()
contextFactory = ssl.DefaultOpenSSLContextFactory('server.key', 'server.crt')

reactor.listenSSL(8000, factory, contextFactory)
reactor.run()
