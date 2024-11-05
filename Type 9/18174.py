file = open('9')
k=0
for str in file:
    a = [int(x) for x in str.split()]
    a.sort()
    pov = [int(x) for x in a if a.count(x) > 1]
    ne_pov = [int(x) for x in a if a.count(x) == 1]
    otr = [int(x) for x in a if x < 0]
    ne_otr = [int(x) for x in a if x > 0]
    if len(pov) == 2 and len(ne_pov) == 4:
        if abs(sum(otr)) > sum(ne_otr):
            k+=1
print(k)

