f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    povtor_3 = [int(x) for x in a if a.count(x)==3]
    not_povtor = [int(x) for x in a if a.count(x)==1]
    if len(povtor_3)==6 and len(not_povtor)==1:
        if max(povtor_3)>max(not_povtor):
            k+=1
print(k)
