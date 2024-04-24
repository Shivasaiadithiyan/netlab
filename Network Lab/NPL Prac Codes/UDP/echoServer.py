from twisted.internet import reactor, protocol

class echoServer(protocol.DatagramProtocol):

    def datagramReceived(self, datagram, addr):
        if datagram.decode() == "CL":
            print("Connection Lost!")
            self.transport.stopListening()
        else:
            print("Message from Client -", datagram.decode(), addr)
            # self.transport.write("Received".encode(), addr)


reactor.listenUDP(8009, echoServer())
reactor.run()