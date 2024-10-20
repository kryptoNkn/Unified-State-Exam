from itertools import product
k = 0
for i in product(sorted(set('МАРИЯ')), repeat=4):
    s = ''.join(i)
    k+=1
    if s == 'АРИЯ':
        print(k)
