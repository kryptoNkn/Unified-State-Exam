# https://inf-ege.sdamgia.ru/problem?id=58235

from itertools import product
alphabet = '0123'
arr = []
for i in product(alphabet, repeat=3):
    if (i[0] != '0' and (int(i[0]) + int(i[2]) > int(i[1]))):
        arr.append(i)
print(len(arr))