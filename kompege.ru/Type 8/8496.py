from itertools import product
k = 0
for i in product(sorted(set('АВОРТ')), repeat=6):
    s=''.join(i)
    k+=1
    if 'ВОРОТА' in s:
        print(k)