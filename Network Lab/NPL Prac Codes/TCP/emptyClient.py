from twisted.internet import reactor, protocol

class echoClient(protocol.Protocol):

    def connectionMade(self):
        with open("/home/ahamed/Documents/NPL Prac Codes/TCP/emptyClientFile.txt", "rb") as file:
            for i in file:
                msg = i
                self.transport.write(msg)

    def dataReceived(self, data):
        print("Acknoledgement from Server -", data.decode())
        self.transport.loseConnection()

class echoFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return echoClient()
    
    def clientConnectionFailed(self, connector, reason):
        print("Connection Failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost")
        reactor.stop()

reactor.connectTCP("localhost", 7006, echoFactory())
reactor.run()