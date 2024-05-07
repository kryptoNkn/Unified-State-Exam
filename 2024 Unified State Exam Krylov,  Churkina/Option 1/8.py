from itertools import product

n = 0
k = 0
for i in product('АВИОРТФ', repeat = 6):
    s = ''.join(i)
    if n % 2 == 0 and s[0] != 'О' and s.count('Р') == 2:
        k += 1
    n += 1
print(k)
