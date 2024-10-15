from itertools import product
n=0
for i in product(sorted(set('ДОСЖ')), repeat = 6):
    s = ''.join(i)
    n+=1
    if s[0] == 'Ж' and s[1] == 'С':
        print(n,s)

# 1793