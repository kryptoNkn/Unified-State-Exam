from itertools import product
k = 0
for i in product(sorted(set('ПАРУС')),repeat=5):
    s = ''.join(i)
    k+=1
    if s.count('У') <= 1 and 'АА' not in s:
        print(k)
        break