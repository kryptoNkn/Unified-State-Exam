from ipaddress import *
net = ip_network('11.92.135.56/255.224.0.0',False)
for ip in net:
    print(ip)
# 1195255254