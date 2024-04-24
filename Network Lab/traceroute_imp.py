from scapy.all import *

def traceroute(destination, max_hops=30):
    # Create a UDP packet with a random source port
    packet = IP(dst=destination, ttl=max_hops) / UDP(sport=RandShort(), dport=33434)

    # Send the packet and wait for a response
    while True:
        # Send the packet and record the start time
        send_time = time.time()
        reply = sr1(packet, verbose=False, timeout=1)

        # If we get a response, print the hop and delay
        if reply is not None:
            print(f'{reply.src}  {time.time()-send_time:.3f} ms')
            # If the response is from the destination, we're done
            if reply.src == destination:
                break

        # If we don't get a response, print a timeout message
        else:
            print('* * *')
        
        # Increment the TTL for the next hop
        packet.ttl += 1

        # If we've exceeded the max number of hops, stop
        if packet.ttl >= max_hops:
            break
        
t1 = traceroute("www.google.com")