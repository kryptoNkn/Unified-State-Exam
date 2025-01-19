from ipaddress import *
net = ip_network('105.224.200.224/255.255.255.224', False)
k = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32)).count('1')%4==0:
        k+=1
print(k)