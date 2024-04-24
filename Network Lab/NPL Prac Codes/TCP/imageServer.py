from twisted.internet import reactor, protocol

class echoServer(protocol.Protocol):

    def dataReceived(self, data):
        print("Image received is saved as serverImage.jpeg")

        with open("serverImage.jpeg", "wb") as file:
            file.write(data)

        ack = f"ACK[clientImage.jpeg]"
        self.transport.write(ack.encode())
        self.transport.loseConnection()

class echoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return echoServer()
    
reactor.listenTCP(9600, echoFactory())
reactor.run()