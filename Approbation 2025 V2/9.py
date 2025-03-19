f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    rp = [int(x) for x in a if a.count(x)==2]
    not_rp = [int(x) for x in a if a.count(x)==1]
    a.sort()
    if a[-1] < a[0]+a[1]+a[2]:
        if len(rp)==2 and len(not_rp)==2:
            k+=1
print(k)