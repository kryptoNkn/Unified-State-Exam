m = []
for x in range(1,2031):
    n = 7**170+7**100-x
    k=0
    while n != 0:
        if n%7==0:
            k+=1
        n//=7
    m.append(k)
    if k == max(m):
        print(x)
# 1715