f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    a.sort()
    if len(set(a))==5 and a[-1]+a[-2]<=a[0]+a[1]+a[2]:
        k+=1
print(k)