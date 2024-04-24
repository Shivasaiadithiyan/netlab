from twisted.internet import reactor, protocol

class echoClient(protocol.Protocol):

    def connectionMade(self):
        with open("/home/ahamed/Documents/NPL Prac Codes/TCP/clientImage.jpeg", "rb") as file:
            img = file.read()
            self.transport.write(img)

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

reactor.connectTCP("localhost", 9600, echoFactory())
reactor.run()