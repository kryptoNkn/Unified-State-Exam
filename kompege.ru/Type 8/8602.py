from itertools import product
k = 0
for i in product(sorted(set('АЕКНС')), repeat = 6):
    s = ''.join(i)
    k+=1
    if 'СЕНЕКА' in s:
        break
print(k)