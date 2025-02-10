# https://inf-ege.sdamgia.ru/problem?id=18558

from itertools import product
alphabet = 'ИВАН'
arr = []
for i in product(alphabet, repeat = 5):
    if i.count('И') >= 1:
        arr.append(i)
print(len(arr))