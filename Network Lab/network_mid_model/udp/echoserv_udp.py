
from twisted.internet.protocol import DatagramProtocol,Factory, Protocol
from twisted.internet import reactor


class EchoUDP(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        self.transport.write(datagram, address)
        print("recieved data:",datagram)
    

        
def main():
    reactor.listenUDP(8000, EchoUDP())
    reactor.run()

if __name__ == '__main__':
    main()