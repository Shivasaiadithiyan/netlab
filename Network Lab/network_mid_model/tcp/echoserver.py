from twisted.internet import protocol,reactor

class echo(protocol.Protocol):
    
    def dataReceived(self, data):
        print("The content is",str(data))
        self.transport.write(data)
    
class echofactory(protocol.Factory):

    def buildProtocol(self, addr):
        return echo()

reactor.listenTCP(8000,echofactory())
reactor.run()