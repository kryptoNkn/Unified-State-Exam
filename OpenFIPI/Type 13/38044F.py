from ipaddress import *
net = ip_network("172.16.176.0/255.255.240.0", False)
k = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32)).count('1')%3 == 0:
        k+=1
print(k)