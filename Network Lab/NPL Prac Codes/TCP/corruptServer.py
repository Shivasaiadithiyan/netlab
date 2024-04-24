from twisted.internet import reactor, protocol

class echoServer(protocol.Protocol):

    def dataReceived(self, data):
        cnt = 0
        if cnt == 2:
            self.transport = None
            self.transport.write(data.decode())
        else:
            print("Message from Client -", data.decode())
            ack = f"ACK[{data.decode()}]"
            self.transport.write(ack.encode())

class echoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return echoServer()
    
reactor.listenTCP(7001, echoFactory())
reactor.run()