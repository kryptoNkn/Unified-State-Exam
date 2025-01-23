f = open('9')
k = 0
for str in f:
    a = [int(x) for x in str.split()]
    razl = [int(x) for x in a if a.count(x)==1]
    a.sort()
    first = len(razl) == 7
    second = (a[0]+a[-1])*2 <= (a[1]+a[2]+a[3]+a[4]+a[5])*3

    if (first+second==1):
        k+=1
print(k)