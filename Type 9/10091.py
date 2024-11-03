f = open('9')
k = 0
for str in f:
    a = [int(x) for x in str.split()]
    a.sort()
    pov = [int(x) for x in a if a.count(x) > 1]
    ne_pov = [int(x) for x in a if a.count(x) == 1]
    if len(pov) == 4 and len(set(pov)) == 2:
        if sum(pov)/4 < sum(a)/7:
            k+=1
print(k)