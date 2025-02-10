from ipaddress import *
net = ip_network("192.168.32.128/255.255.255.192", False)
count = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32)).count('1') % 2 == 0:
        count+=1
print(count)