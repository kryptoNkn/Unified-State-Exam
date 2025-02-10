# https://inf-ege.sdamgia.ru/problem?id=58237

from itertools import product
alphabet = '0123456'
arr = []
for i in product(alphabet, repeat=4):
    if i[0] > i[1] > i[2] > i[3]:
        arr.append(i)
print(len(arr))