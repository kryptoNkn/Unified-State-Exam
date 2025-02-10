# https://inf-ege.sdamgia.ru/problem?id=10500

from itertools import product

alphabet = '12345'
arr = []
for i in product(alphabet, repeat=5):
    if i.count('1') == 3:
        arr.append(i)
print(len(arr))