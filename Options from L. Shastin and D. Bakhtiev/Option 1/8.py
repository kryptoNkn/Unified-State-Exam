from itertools import product
k=0
for i in product(sorted(set('СЕНТЯБРЬ')), repeat=5):
    s = ''.join(i)
    k+=1
    if s[0]=='Р' and 'Ь' not in s:
        print(k)
# 16384