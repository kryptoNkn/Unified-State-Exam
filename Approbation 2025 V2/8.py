from itertools import product
k = 0
for i in product('012345678', repeat=5):
    s = ''.join(i)
    if s[0]!='0' and s.count('0')==1:
        if '01' not in s and '10' not in s and '03' not in s and '30' not in s and '05' not in s and '50' not in s and '07' not in s and '70' not in s:
            k+=1
print(k)