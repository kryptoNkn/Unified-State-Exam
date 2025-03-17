f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    a1 = [int(x) for x in a if a.count(x)==1]
    a3 = [int(x) for x in a if a.count(x)==3]
    if len(a1)==3 and len(a3)==3:
        if sum(a3)**2 > sum(a1)**2:
            k+=1
print(k)