
"""code by G.O.A.T"""

# from twisted.internet import reactor, protocol
# import struct
# import socket
# class ARPTable:
#     def __init__(self):
#         self.table = {}

#     def add_entry(self, ip_address, mac_address):
#         self.table[ip_address] = mac_address

#     def get_mac_address(self, ip_address):
#         return self.table.get(ip_address)

# class ARPServer(protocol.DatagramProtocol):
#     def __init__(self, arp_table):
#         self.arp_table = arp_table

#     def datagramReceived(self, data, address):
#         # Parse the ARP packet
#         hw_type, proto_type, hw_len, proto_len, op_code, src_hw_addr, src_proto_addr, dst_hw_addr, dst_proto_addr = struct.unpack("!HHBBH6s4s6s4s", data)

#         # Handle ARP requests
#         if op_code == 1:
#             mac_address = self.arp_table.get_mac_address(dst_proto_addr)
#             if mac_address:
#                 # Construct an ARP reply packet
#                 arp_reply = struct.pack("!HHBBH6s4s6s4s", hw_type, proto_type, hw_len, proto_len, 2, mac_address, dst_proto_addr, src_hw_addr, src_proto_addr)
#                 self.transport.write(arp_reply, address)

# class RARPServer(protocol.DatagramProtocol):
#     def __init__(self, arp_table):
#         self.arp_table = arp_table

#     def datagramReceived(self, data, address):
#         # Parse the RARP packet
#         hw_type, proto_type, hw_len, proto_len, op_code, src_hw_addr, src_proto_addr = struct.unpack("!HHBBH6s4s", data)

#         # Handle RARP requests
#         if op_code == 3:
#             ip_address = socket.inet_ntoa(src_proto_addr)
#             mac_address = self.arp_table.get_mac_address(ip_address)
#             if mac_address:
#                 # Construct a RARP reply packet
#                 rarp_reply = struct.pack("!HHBBH6s4s", hw_type, proto_type, hw_len, proto_len, 4, mac_address, src_proto_addr)
#                 self.transport.write(rarp_reply, address)

# arp_table = ARPTable()
# arp_table.add_entry("192.168.1.1", "00:11:22:33:44:55")

# arp_server = ARPServer(arp_table)
# rarb_server = RARPServer(arp_table)

# reactor.listenUDP(67, arp_server)
# reactor.listenUDP(68, rarb_server)

# reactor.run()


"""code by arun not sure whether it is correct or not"""

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