from itertools import product
k = 0
for i in product('012345678', repeat=7):
    s = ''.join(i)
    if s[0]!='0' and s[0]!='2' and s[0]!='4' and s[0]!='6':
        if not s[-1]==s[-2]==s[-3]:
            k+=1
print(k)


