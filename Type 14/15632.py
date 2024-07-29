# https://inf-ege.sdamgia.ru/problem?id=15632

x = 4 ** 14 + 2 ** 32 - 4
s = bin(x)[2:]
print(s.count('1'))

# Solution: 27