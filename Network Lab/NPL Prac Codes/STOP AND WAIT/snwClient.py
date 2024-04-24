from twisted.internet import reactor, protocol

class StopAndWaitClient(protocol.Protocol):

    def connectionMade(self):
        self.sendData()

    def sendData(self):
        if self.transport.connected:
            data = input("Enter data/quit to Server: ")
            if data == 'q':
                self.transport.write(data.encode())
                self.transport.loseConnection()
                return
            self.transport.write(data.encode())
            self.timeout = reactor.callLater(7, self.resendData)

    def resendData(self):
        print("Timeout, Rend the Data.")
        if self.transport.connected:
            self.sendData()

    def dataReceived(self, data):
        print("Acknowledge from Server -", data.decode())
        if self.timeout.active():
            self.timeout.cancel()
        self.sendData()

class StopAndWaitClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return StopAndWaitClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

reactor.connectTCP('localhost', 8081, StopAndWaitClientFactory())
reactor.run()