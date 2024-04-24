from twisted import reactor, protocol

class Bus(protocol.Protocol):
    
    def __init__(self, factory):
        self.factory = factory
        
    def make_connection(self, client):
        self.factory.client.add(client)
        
    def remove_connection(self):
        self.factory.client.remove(self)
        
    def data_transfer(self, data):
        for client in self.factory.client:
            if client != self:
                client.transport.write(data)
                
class Bus_Factory(protocol.Factory):
    
    def build_protocol(self):
        return Bus()
    
reactor.listenTCP(8000, Bus_Factory())
reactor.run()