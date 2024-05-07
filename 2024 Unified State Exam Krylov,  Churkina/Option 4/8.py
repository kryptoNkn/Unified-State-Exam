from itertools import product

n = 0
k = 0
for i in product("АГЕИЛНРТ", repeat = 5):
    s = ''.join(i)
    n += 1
    if n % 2 != 0 and s[0] != 'Т' and 1 <= s.count('Н') <= 2:
        k += 1
print(k)


