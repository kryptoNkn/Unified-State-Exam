from itertools import product
k=0
for i in product(sorted(set('КОТБУС')), repeat=8):
    s = ''.join(i)
    if (s[0]!='О' and s[0]!='У') and 'КОТ' in s:
        k+=1
print(k)
