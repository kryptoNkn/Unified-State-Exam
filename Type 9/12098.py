f = open('9')
k = 0
for str in f:
    a = [int(x) for x in str.split()]
    povtor_tri = [int(x) for x in a if a.count(x)==3]
    povtor_ne_4etn = [int(x) for x in a if a.count(x)>1 and x%2!=0]
    nepovtor_chetn = [int(x) for x in a if a.count(x)==1 and x%2==0]
    if len(povtor_tri) == 3:
        if len(povtor_ne_4etn)==3:
            if len(nepovtor_chetn)==1:
                k+=1
print(k)