file = open('9')
k = 0
for str in file:
    a = [int(x) for x in str.split()]
    ne_povtor = [int(x) for x in a if a.count(x) == 1]
    povtor_3 = [int(x) for x in a if a.count(x) == 3]
    if len(povtor_3) == 3 and len(ne_povtor) == 3:
        if sum(povtor_3)**2 > sum(ne_povtor)**2:
            k+=1
print(k)