from itertools import product
k=0
for i in product(sorted(set('МАРТ')), repeat=4):
    s=''.join(i)
    k+=1
    if s[0]=='М':
        print(k)
        break