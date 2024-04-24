from twisted.internet import protocol
from twisted.protocols import basic
from twisted.application import service, internet

class Chat(basic,LineReciever):
    
    def make_connection(self):
        print("Client Connection Established")
        self.factory.clients.add(self)
        
    def remove_connection(self):
        print("Client Connection lost")
        self.factory.clients.remove(self)
        
    def line_received(self, line):
        print("Recieved Message -", repr(line))
        for i in self.factory.clients:
            i.message(line)
            
    def message(self, msg):
        self.transport.write(msg + b"\n")
        
factory = protocol.ServerFactory()
factory.protocol = Chat
factory.clients = []

application = service.Application("chatserver")

