from itertools import product

k=0
for i in product('0123', repeat=5):
    s = ''.join(i)
    if s[0]!= '0' and s.count('3') == 1 and '30' not in s and '03' not in s:
        k+=1
print(k)