from itertools import product
k=0
for i in product(sorted(set('ПОБЕДА')), repeat = 6):
    s = ''.join(i)
    k+=1
    if s[0]=='О' and s.count('П')==1 and s.count('О')==1 and s.count('Б')==1 and s.count('Е')==1 and s.count('Д')==1 and s.count('А')==1:
        print(k,s)
# 38306