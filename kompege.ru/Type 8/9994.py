from itertools import product
k = 0
for i in product(sorted(set('ШКОЛА')),repeat=5):
    s = ''.join(i)
    k+=1
    if 'ШАЛАШ' in s:
        print(k)