from itertools import product

n = 0
k = 0
for i in product('АГИЛМНОФ', repeat = 5):
    s = ''.join(i)
    n += 1
    if n % 2 != 0 and s[0] != 'Н' and s.count('О') <= 1:
        k += 1
print(k)
