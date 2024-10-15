from itertools import product
k=0
for i in product(sorted(set('БМЮРН')), repeat = 6):
    s = ''.join(i)
    k+=1
    if k%2!=0 and s[0] != 'М' and s.count('Р') >= 2 and 'Ю' not in s:
        print(k)

# 11719