from itertools import product
k = 0
for i in product('0123456789ABCDE', repeat=5):
    s = ''.join(i)
    if s[0]!='0' and s.count('8')==1 and s.count('A')+s.count('B')+s.count('C')+s.count('D')+s.count('E')>=2:
        k+=1
print(k)
