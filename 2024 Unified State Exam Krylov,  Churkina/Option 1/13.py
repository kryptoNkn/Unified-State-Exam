from ipaddress import *
ip_net = ip_network("142.108.56.118/255.255.255.240", False)
count = 0
for i in ip_net:
    if bin(int(i))[-16:].count("1") > bin(int(i))[:-16].count("1"):
        count += 1
print(count)