f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    povtor1 = [int(x) for x in a if a.count(x)==1]
    ne_povtor=[int(x) for x in a if a.count(x)==3]
    if len(ne_povtor)==3 and len(povtor1)==3:
        if sum(ne_povtor)**2 > sum(povtor1)**2:
            k+=1
print(k)