# Normal Python code is made to be look like twisted python

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
class ARP(Protocol):
    def __init__(self,arp_table):
        self.arp=arp_table

    def add_entry(self,ip,mac):
        self.arp[ip]=mac
        
    def getmac(self,ip):
        return self.arp[ip]
    
class RARP(Protocol):
    def __init__(self,arp_tabel):
        self.rarp=arp_tabel

    def getip(self,mac):
        
        for i in self.rarp:
            if self.rarp[i]==mac:
                return self.rarp[i]
            else:
                continue
        else:
            print("invalid mac address")


tab=ARP({})
tab.add_entry("192.168.1.1", "00:11:22:33:44:55")

# arp_server=ARP()
# rarp_server=RARP()

print(tab.getmac("192.168.1.1"))

#print(rarp_server.getip("00:11:22:33:44:55"))