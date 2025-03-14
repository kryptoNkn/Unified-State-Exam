from itertools import product
k=0
for i in product(sorted(set('ЛЮСТРА')), repeat=5):
    s = ''.join(i)
    if s.count('Ю') <= 2 and (s[-1]!='Л' and s[-1]!='С' and s[-1]!='Т' and s[-1]!='Р'):
        k+=1
print(k)