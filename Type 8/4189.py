from itertools import product
k = 0
for i in product(sorted(set('БАТЫР')), repeat = 5):
    s = ''.join(i)
    k+=1
    if 'Ы' not in s and 'АА' not in s:
        print(k, s)
# 131