from ipaddress import *
net = ip_network("122.159.136.144/255.255.255.248", False)
k = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32)).count('1')%4!=0:
        k+=1
print(k)