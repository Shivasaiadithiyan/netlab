from twisted.internet import reactor, protocol

class echoServer(protocol.Protocol):

    def dataReceived(self, data):
        print("Message from Client -", data.decode())
        ack = f"ACK[{data.decode()}]"
        self.transport.write(ack.encode())

class echoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return echoServer()
    
reactor.listenTCP(8033, echoFactory())
reactor.run()