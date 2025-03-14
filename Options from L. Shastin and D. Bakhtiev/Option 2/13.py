from ipaddress import *
net = ip_network('123.222.111.192/255.255.255.248')
k=0
for ip in net:
    if bin(int(ip))[2:].zfill(32).count('0')%3!=0:
        k+=1
print(k)
