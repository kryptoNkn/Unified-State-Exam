# https://inf-ege.sdamgia.ru/problem?id=13627

x = 4 ** 511 + 2 ** 511 - 511
s = bin(x)[2:]
print(s.count('1'))

# Solution: 504