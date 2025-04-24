f = open('9')
for str in f:
    a = [int(x) for x in str.split()]
    if a[0]>a[1]>a[2]>a[3]>a[4]>a[5]>a[6]:
        a.sort()
        if (max(a)+min(a))//2 > (a[1]+a[2]+a[3]+a[4]+a[5])//5:
            print(a,sum(a))
            break
# 652