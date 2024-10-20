from itertools import product
k = 0
for i in product(sorted(set('ЩЭДСР')), repeat=4):
    s = ''.join(i)
    k+=1
    if 'ЩДЩД' in s:
        print(k)