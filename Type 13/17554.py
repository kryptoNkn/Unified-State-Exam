from ipaddress import *
net = ip_network("112.160.0.0/255.240.0.0", False)
count = 0
for ip in net:
    if (bin(int(ip))[2:].zfill(32)).count('1') % 3 != 0:
        count+=1
print(count)