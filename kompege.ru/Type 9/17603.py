f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    unique = [int(x) for x in a if a.count(x)==1]
    a.sort()
    if len(unique)==4 and a[0]+a[-1] > a[1]+a[2]:
        k+=1
print(k)