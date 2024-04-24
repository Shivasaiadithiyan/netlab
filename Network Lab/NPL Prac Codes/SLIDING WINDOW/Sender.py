from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor, task

class Sender(DatagramProtocol):
    def __init__(self):
        self.seq_num = 0
        self.window_size = 4
        self.base = 0
        self.timer = None
        self.packets = [
            b"Packet 0",
            b"Packet 1",
            b"Packet 2",
            b"Packet 3",
            b"Packet 4",
            b"Packet 5",
            b"Packet 6",
            b"Packet 7"
        ]
        self.sent = [False] * len(self.packets)

    def startProtocol(self):
        self.sendPackets()

    def sendPackets(self):
        while self.seq_num < min(self.base + self.window_size, len(self.packets)):
            if not self.sent[self.seq_num]:
                print("Sending packet", self.seq_num)
                self.transport.write(self.packets[self.seq_num], ("127.0.0.1", 8000))
                #print(f'SP SEQ:{self.seq_num} BASE: {self.base} TIME:{self.timer}')
                if self.base == self.seq_num:
                    self.startTimer()
                self.sent[self.seq_num] = True
            self.seq_num += 1

    def startTimer(self):
        if self.timer is not None and self.timer.active():
            self.timer.cancel()
        self.timer = reactor.callLater(5, self.handleTimeout)

    def handleTimeout(self):
        print("Timeout, resending packets from", self.base)
        self.seq_num = self.base
        # print(f'SEQ :{self.seq_num},BASE:{self.base}')
        for i in range(self.seq_num,self.window_size + 1) :
            self.sent[i] = False
            
        self.sendPackets()

    def datagramReceived(self, datagram, address):

        ack_num = int(datagram.decode())
        print("Received ACK", ack_num)
        if ack_num >= self.base:
            self.base = ack_num + 1
            if self.base == self.seq_num:
                if self.timer is not None and self.timer.active():
                    self.timer.cancel()
                self.sendPackets()
            else:
                self.startTimer()

if __name__ == "__main__":
    reactor.listenUDP(9000, Sender())
    reactor.run()