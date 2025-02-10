# https://inf-ege.sdamgia.ru/problem?id=10473

from itertools import product
a = '1234'
arr = []
for i in product(a, repeat=5):
    if i.count('1') == 2:
        arr.append(i)
print(len(arr))
    