from itertools import product
k = 0
for i in product(sorted(set('СОРНЯК')), repeat=6):
    s = ''.join(i)
    k+=1
    if s.count('К') <= 3 and s.count('Я') == 2:
        print(k)
        break
