from itertools import product
k=0
for i in product('01234567', repeat=7):
    s = ''.join(i)
    if s[0]!='0' and s.count('0')==2:
        for j in '0246':
            s = s.replace(j,'*')
        for j in '1357':
            s = s.replace(j,'-')
        if '**' not in s and '--' not in s:
            k+=1
print(k)
