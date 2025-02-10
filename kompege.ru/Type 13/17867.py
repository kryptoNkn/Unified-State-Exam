from ipaddress import *
net = ip_network("172.16.168.0/255.255.248.0", False)
count = 0
for ip in net:
    if(bin(int(ip))[2:].zfill(32)).count('1') % 5 !=0:
        count+=1
print(count)