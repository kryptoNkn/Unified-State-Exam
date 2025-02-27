f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    a.sort()
    var1 = (a[0]+a[1]+a[2]+a[3]+a[4]==18)
    var2 = ((a[0]+a[1]+a[2]+a[3]+a[4])%18==0)

    if (var1==True) or (var2==True) or (var1==True and var2==True):
        k+=1
print(k)