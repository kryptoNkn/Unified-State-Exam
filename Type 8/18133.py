from itertools import product
k = 0
for i in product(sorted(set('КОДИМ')), repeat=5):
    s = ''.join(i)
    k+=1
    if s.count('М') == 2 and 'ММ' not in s:
        print(k)
# 3099