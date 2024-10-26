from itertools import product
k = 0
a = []
for i in product(sorted(set('КОФЕ')), repeat = 5):
    s = ''.join(i)
    k+=1
    if s.count('О') == 1 and 'КО' not in s and 'ОК' not in s and 'ОФ' not in s and 'ФО' not in s:
        a.append(k)
        print(min(a) + max(a))
# 1014