from math import prod

f = open('9')
k=0
for str in f:
    a = [int(x) for x in str.split()]
    povtor_2 = [int(x) for x in a if a.count(x) == 2]
    ostalnie_3 = [int(x) for x in a if a.count(x) == 1]
    vse_povtor = [int(x) for x in a if a.count(x) > 1]
    ne_povtor = [int(x) for x in a if a.count(x) == 1]
    if len(povtor_2)==4 and len(ostalnie_3)==3 and prod(vse_povtor) > 2* prod(ne_povtor):
        k+=1
print(k)
