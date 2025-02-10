from itertools import product
k = 0
count = 0
for i in product(sorted(set('АОЖПЮЗ')), repeat=6):
    s = ''.join(i)
    count += 1
    if s[0] == 'А' and s.count('З') >= 2 and count % 2 == 0:
        k += 1
print(k)