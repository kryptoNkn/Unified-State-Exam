from itertools import product
k = 0
for i in product('0123456789ABCD', repeat=5):
    s = ''.join(i)
    if s[0]!='0' and s.count('9')==1 and s.count('B')+s.count('C')+s.count('D') <= 3:
        k+=1
print(k)