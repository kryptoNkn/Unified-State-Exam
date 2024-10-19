from itertools import product
k = 0
for i in product('012345678',repeat=7):
    s = ''.join(i)
    if s[0]!='0' and s.count('8') == 1:
        if s[0] == '0' or s[0] == '2' or s[0] == '4' or s[0] == '6' or s[0]=='8':
            if s[-1] == '1' or s[-1] == '3' or s[-1]=='5' or s[-1]=='7':
                k+=1
print(k)
