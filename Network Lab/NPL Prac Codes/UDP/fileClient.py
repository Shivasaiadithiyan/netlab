from twisted.internet import reactor, protocol
import pickle

class echoClient(protocol.DatagramProtocol):

    def startProtocol(self):
        self.transport.connect("127.0.0.1", 8034)
        self.sendDatagram()

    def sendDatagram(self):
        with open("UDP/clientFile.txt", "r+") as file:
            data = file.read()
            self.transport.write(pickle.dumps(data))
        print("File Transferred!")
        print("Connection Lost!")
        
reactor.listenUDP(0, echoClient())
reactor.run()