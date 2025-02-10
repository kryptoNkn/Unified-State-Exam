f = open('9')
k = 0
for str in f:
    a = [int(x) for x in str.split()]
    pov = [int(x) for x in a if a.count(x) == 2]
    ne_pov = [int(x) for x in a if a.count(x) == 1]
    if len(pov) == 6 and len(ne_pov) == 1:
        if (max(pov) + min(pov)) // 2 < ne_pov[0]:
            k+=1
print(k)
