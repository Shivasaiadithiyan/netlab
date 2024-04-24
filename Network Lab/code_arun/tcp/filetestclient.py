from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):

    def connectionMade(self):
        with open("sample.txt", "r+") as file:
            for i in file:
                msg = i
        # msg = input("Enter the message to Server - ")
                self.transport.write(msg.encode())

    def dataReceived(self, data):
        print ("Acknoledgement from Server -", data.decode())
        self.transport.loseConnection()
    
class EchoFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print ("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print ("Connection lost.")
        reactor.stop()
    
reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()