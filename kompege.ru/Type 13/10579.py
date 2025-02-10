from ipaddress import *
net = ip_network("192.168.240.0/255.255.255.0", False)
count = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32)).count('1') == (bin(int(ip))[2:].zfill(32)).count('0'):
        count+=1
print(count)