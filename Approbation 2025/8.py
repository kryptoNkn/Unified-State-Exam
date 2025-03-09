from itertools import product
k = 0
for i in product(sorted(set('ФОКУС')), repeat=5):
    s = ''.join(i)
    k += 1
    if 'Ф' not in s and s.count('У')==2:
        print(k)
# 2313