import re

d = {"192.2.2.3":"255.255.254.0"}
for i in d:
    l1 = i.split(".")
    l1[-1] = "0"
    print("Network Address -", ".".join(l1))
    l2 = i.split(".")
    l2[-1] = "255"
    print("Broadcast Address -", ".".join(l2))
    sm = d[i]
    l3 = sm.split(".")
    binary = []
    for i in l3:
        binary.append(format(int(i), "08b"))
    bsm = ".".join(binary)
    z = re.findall(r"0", bsm)
    host = (2**len(z)) - 2
    print("No. of Hosts -", host)