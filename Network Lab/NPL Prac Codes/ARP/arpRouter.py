from twisted.internet import reactor, protocol

class EchoServer(protocol.Protocol):
    def __init__(self,factory):
        self.factory = factory

    def connectionMade(self):
        self.c=0
        self.factory.clients.append(self)
        print("Client connected")

    # def connectionLost(self, reason):
    #     self.factory.clients.remove(self)
    #     print("Client disconnected")

    def dataReceived(self, data):
        if data!=b'hi':
            print("mac:",data.decode())
        else:
            flag = str(input("Want to request - "))
            if flag == "y":
                ip = str(input("Enter the IP - "))
                self.broadcast(ip)
                self.c=1

    # def requestMAC(self, host_ip):
    #     self.transport.write(host_ip.encode())

    def broadcast(self, data):

        for client in self.factory.clients:
            # print('h')
            client.transport.write(data.encode())

class EchoFactory(protocol.Factory):
    def __init__(self):
        self.clients=[]
    def buildProtocol(self, addr):
        return EchoServer(self)

reactor.listenTCP(9014, EchoFactory())
reactor.run()