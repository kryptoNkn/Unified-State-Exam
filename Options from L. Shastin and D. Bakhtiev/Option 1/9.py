f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    okonch_5 = [int(x) for x in a if x%10==5]
    a.sort()
    if (a[-1]+a[-2])*2 > (a[0]+a[1]+a[2])*3:
        if len(okonch_5)>=2:
            k+=1
print(k)