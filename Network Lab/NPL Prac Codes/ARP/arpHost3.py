from twisted.internet import reactor, protocol
import pickle

class echoClient(protocol.Protocol):

    def __init__(self):
        self.ip = "34.4.2.3"
        self.mac = "AB:3"
        
    def connectionMade(self):
        # msg = {self.ip:self.mac}
        # self.transport.write(pickle.dumps(msg))
        self.transport.write(b'hi')
    def dataReceived(self, data):
        print("Msg from Server - ", data.decode())
        self.replyMAC(data.decode())

    def replyMAC(self, host_ip):
        if host_ip == self.ip:
            self.transport.write(self.mac.encode())
            self.transport.loseConnection()
        else:
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

reactor.connectTCP("localhost", 9013, echoFactory())
reactor.run()