from twisted.internet import reactor, protocol

class StopAndWaitServer(protocol.Protocol):
    def dataReceived(self, data):
        if data.decode() == "q":
            print("Client Disconnected!")
            self.transport.loseConnection()
        else:
            print("Message from Client -", data.decode())
            flag = str(input("Acknowledge or Not - "))
            if flag == "y":
                ack = f"ACK[{data.decode()}]"
                self.transport.write(ack.encode())

class StopAndWaitServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return StopAndWaitServer()

reactor.listenTCP(8081, StopAndWaitServerFactory())
reactor.run()