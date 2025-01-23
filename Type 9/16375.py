file = open('9')
k = 0
for str in file:
    a = [int(x) for x in str.split()]
    povtor = [int(x) for x in a if a.count(x)==2]
    ne_povtor = [int(x) for x in a if a.count(x)==1]
    ne_povtor.sort()
    if len(povtor)==2 and len(ne_povtor)==5:
        if ne_povtor[0]*ne_povtor[1]*ne_povtor[2] > povtor[0]**2:
            k+=1
print(k)
