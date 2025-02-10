from itertools import product
k = 0
for i in product(sorted(set('МАНГУСТ')), repeat=6):
    s = ''.join(i)
    k+=1
    if s[0]!='У' and s.count('М')==2 and s.count('Г')<=1:
        print(k)
# 100810