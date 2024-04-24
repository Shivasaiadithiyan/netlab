from twisted.internet import reactor, protocol

class echoServer(protocol.Protocol):

    def dataReceived(self, data):
        with open("/home/ahamed/Documents/NPL Prac Codes/TCP/serverFile.txt", "w+") as file:
            file.write(data.decode())
        print("Message from Client -", data.decode())
        ack = f"ACK[{data.decode()}]"
        self.transport.write(ack.encode())

class echoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return echoServer()
    
reactor.listenTCP(9301, echoFactory())
reactor.run()