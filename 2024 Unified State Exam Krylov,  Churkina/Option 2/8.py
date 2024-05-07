from itertools import product

n = 0
k = 0
for i in product("АЕИКЛПР", repeat = 6):
    s = ''.join(i)
    n += 1
    if n % 2 == 0 and s[0] != "К" and s.count('И') >= 2:
        k += 1
print(k)