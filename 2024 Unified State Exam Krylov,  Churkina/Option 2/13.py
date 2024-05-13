from ipaddress import *

ip_net = ip_network("116.29.170.89/255.255.255.224", False)
count = 0
for ip in ip_net:
    bin_ip = f"{ip:b}"
    if bin_ip[:16].count('1') >= bin_ip[16:].count('1'):
        count += 1
print(count)