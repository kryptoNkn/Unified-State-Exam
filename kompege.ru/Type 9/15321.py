f = open('9')
k = 0
for str in f:
    a = [int(x) for x in str.split()]
    a.sort()
    if a[-1] < a[0]+a[1]+a[2]:
        if (a[0]+a[1]==a[2]+a[3]) or (a[1]+a[2]==a[0]+a[3]) or (a[1]+a[3]==a[0]+a[2]):
            k+=1
print(k)