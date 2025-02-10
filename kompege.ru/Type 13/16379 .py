from ipaddress import *
net = ip_network("112.208.0.0/255.255.128.0", False)
count = 0
for ip in net:
    if (bin(int(ip)).zfill(32)).count('1') % 11 == 0:
        count+=1
print(count)