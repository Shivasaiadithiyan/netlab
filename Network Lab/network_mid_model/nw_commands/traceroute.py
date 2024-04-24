from twisted.internet import reactor, defer
from twisted.internet.protocol import DatagramProtocol

class Traceroute(DatagramProtocol):
    def __init__(self, target, max_hops=30, timeout=1):
        self.target = target
        self.max_hops = max_hops
        self.timeout = timeout
        self.current_hop = 1
        self.deferred = defer.Deferred()
    
    def startProtocol(self):
        self.transport.connect(self.target, 80)
        self.sendPacket()
    
    def sendPacket(self):
        self.transport.write(bytes([self.current_hop]), (self.target, 80))
        reactor.callLater(self.timeout, self.checkTimeout)
    
    def checkTimeout(self):
        if not self.deferred.called:
            self.deferred.errback(Exception("Request timed out"))
    
    def datagramReceived(self, datagram, addr):
        if addr[0] == self.target:
            self.deferred.callback(addr)
        elif self.current_hop < self.max_hops:
            self.current_hop += 1
            self.sendPacket()
        else:
            self.deferred.errback(Exception("Max hops reached"))
            self.transport.stopListening()
            reactor.stop()

def traceroute(target):
    traceroute = Traceroute(target)
    return traceroute.deferred

if __name__ == '__main__':
    d = traceroute('www.google.com')
    d.addCallbacks(print, print)
    reactor.run()
