from itertools import product
k = 0
for i in product(sorted(set("ФЕВРАЛЬ")), repeat = 6):
    s = ''.join(i)
    k+=1
    if 'Е' not in s and 'А' not in s:
        print(k, s)
# 19609