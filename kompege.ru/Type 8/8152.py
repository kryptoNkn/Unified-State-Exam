from itertools import product
k = 0
for i in product(sorted(set('ЛИНКОР')), repeat=4):
    s = ''.join(i)
    k+=1
    if 'КИНО' in s:
        print(k)