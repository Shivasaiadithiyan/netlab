from twisted.internet import reactor, protocol

class echoClient(protocol.Protocol):

    def connectionMade(self):
        n = int(input("Enter the number of communications - "))
        for i in range(n):
            msg = input("Enter the message to the server - ")
            self.transport.write(msg.encode())

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

reactor.connectTCP("localhost", 7002, echoFactory())
reactor.run()