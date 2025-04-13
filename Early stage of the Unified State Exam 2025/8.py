from itertools import product
k=0
for i in product(sorted(set('ДГИАШЭ')), repeat=5):
    s = ''.join(i)
    if s[0]!='И' and s[0]!='А' and s[0]!='Э':
        if s[-1]!='Д' and s[-1]!='Г' and s[-1]!='Ш':
            k+=1
print(k)