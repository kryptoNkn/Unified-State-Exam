from itertools import product
k=0
for i in product('АЗИМНОПРТ', repeat = 5):
    s = ''.join(i)
    k+=1
    if k%2==0 and s[0] == 'Н' and s.count('Р') == 2:
        print(k,s)

# 32712
