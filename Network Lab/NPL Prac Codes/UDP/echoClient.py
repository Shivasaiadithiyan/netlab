from twisted.internet import reactor, protocol

class echoClient(protocol.DatagramProtocol):

    def startProtocol(self):
        self.transport.connect("127.0.0.1", 8009)
        self.sendDatagram()

    def sendDatagram(self):
        flag = str(input("Want to send - "))
        if flag == "y":
            datagram = input("Enter the message to Server - ")
            self.transport.write(datagram.encode())
            self.sendDatagram()
        else:
            print("Connection Lost!")
            self.transport.write("CL".encode())
            self.transport.stopListening()

    def datagramReceived(self, datagram: bytes, addr):
        print(datagram.decode())
        
reactor.listenUDP(0, echoClient())
reactor.run()