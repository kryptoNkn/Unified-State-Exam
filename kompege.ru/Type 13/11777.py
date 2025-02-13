from ipaddress import *
net = ip_network('119.124.96.0/255.255.240.0', False)
k = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32))[-2]=='0':
        k+=1
print(k)