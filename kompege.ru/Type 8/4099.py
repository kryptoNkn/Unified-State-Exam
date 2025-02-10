from itertools import product
k = 0
for i in product(sorted(set('БУЛКА')), repeat = 4):
    s = ''.join(i)
    k+=1
    if len(set(s)) == 4:
        print(k,s)
# 587