from itertools import product
n=0
for i in product(sorted(set('ЩРЮИ')), repeat=5):
    s = ''.join(i)
    n+=1
    if s[0] == 'Щ' and s[-1] == 'И':
        print(n)

# 765
