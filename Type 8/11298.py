from itertools import product
k=0
count = 0
for i in product(sorted(set('АОЖПЮЗ')), repeat=6):
    s = ''.join(i)
    k+=1
    if k % 2 == 0 and s[0] == 'А' and s.count('З') >= 2:
        count+=1
print(count)
