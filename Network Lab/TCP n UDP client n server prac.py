from twisted.internet import reactor, protocol

class EchoClient_TCP(protocol.Protocol):
    
    def make_connection(self):
        self.transport.write(b"Hello Server")
        
    def data_from_server(self, data):
        print('Received Data -', data)
        self.transport.write(data)
        self.transport.loseConnection()
        
class EchoClientFactory_TCP(protocol.Factory):
    
    def build_protocol(self):
        return EchoClient_TCP()
    
    def connection_failed(self):
        print("Connection Failed")
        reactor.stop()
        
    def connection_lost(self):
        print("Connection Lost")
        reactor.stop()
        
reactor.listenTCP(8000, EchoFactory_TCP())
reactor.run


class EchoServer_TCP(protocol.Protocol):
    
    def datareceived(self, data):
        self.transport.write(data)
        
class EchoServerFactory_TCP(protocol.Factory):
    
    def build_protocol(self):
        return EchoServer_TCP()
    
reactor.listenTCP(8000, EchoServerFactory_TCP())
reactor.run()