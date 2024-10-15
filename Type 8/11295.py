from itertools import product
n=0
for i in product(sorted(set('ЩЭДСР')), repeat = 4):
    s = ''.join(i)
    n+=1
    if 'ЩДЩД' in s:
        print(n)