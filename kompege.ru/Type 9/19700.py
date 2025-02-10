f = open('9')
k = 0
for str in f:
    a = [int(x) for x in str.split()]
    double_repeat = [int(x) for x in a if a.count(x)==2]
    not_repeat = [int(x) for x in a if a.count(x)==1]
    a.sort()
    if len(set(double_repeat))==1 and len(not_repeat)==3:
        if a[0]+a[-1] < a[1]+a[2]+a[3]:
            k+=1
print(k)
