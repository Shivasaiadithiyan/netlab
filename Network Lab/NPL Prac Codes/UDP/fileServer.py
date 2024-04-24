from twisted.internet import reactor, protocol
import pickle

class echoServer(protocol.DatagramProtocol):

    def datagramReceived(self, datagram, addr):
        with open("/home/ahamed/Documents/NPL Prac Codes/UDP/serverFile.txt", "w+") as file:
            file.write(pickle.loads(datagram))
        print("File Received!")
        print("Client Disconnected!")
        reactor.stop()

reactor.listenUDP(8034, echoServer())
reactor.run()