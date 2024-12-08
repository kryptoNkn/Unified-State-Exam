from ipaddress import *
net = ip_network("192.168.32.160/255.255.255.240", False)
count = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32)).count('0') > 21:
        count+=1
print(count)