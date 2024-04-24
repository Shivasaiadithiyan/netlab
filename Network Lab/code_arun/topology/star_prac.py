from twisted import protocol, reactor

class Star_Server(protocol.Protocol):
    
    def __init__(self):
        self.clients = set()
        
    def make_connection(self, client):
        self.clients.add(client)

    def remove_connection(self, reason):
        self.clients.remove(self)
        
    def send_data_received(self, data):
        for client in self.clients:
            if client is not self:
                client.transport.write(data)
        
class Star_Factory(protocol.Factory):
    
    def build_protocol(self, addr):
        return Star_Server()
    
reactor.listenTCP(8000, Star_Factory())
reactor.run()