from itertools import product
k = 0
for i in product(sorted(set('ПЯТЬДНЕЙ')), repeat = 4):
    s = ''.join(i)
    k+=1
    if "Я" not in s and "Е" not in s and s.count('П')<=1 and s.count('Т')<=1 and s.count('Ь')<=1 and s.count('Д')<=1 and s.count('Н')<=1 and s.count('Й')<=1:
        print(k)
# 3428
