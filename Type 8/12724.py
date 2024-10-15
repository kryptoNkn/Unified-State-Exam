from itertools import *
k=0
for i in product(sorted(set('КАЛЕЙДОСКОП'), reverse=1),repeat = 6):
    s = ''.join(i)
    if k%2==0 and s[0] == 'К' and s.count('Й') >= 2 and 'С' not in s and 'Е' not in s:
        print(k,s)
    k += 1

# 243698
