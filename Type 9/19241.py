f = open('9')
k = 0
for str in f:
    a = [int(x) for x in str.split()]
    povtor_3 = [int(x) for x in a if a.count(x)==3]
    ne_povtor_5 = [int(x) for x in a if a.count(x)==1]
    k += 1
    if len(povtor_3) == 6 and len(set(povtor_3))==2:
        if sum(povtor_3)//6 < ne_povtor_5[0]:
            print(k)

