# https://inf-ege.sdamgia.ru/problem?id=8664

x = 8 ** 2020 + 4 ** 2017 + 26 - 1
s = bin(x)[2:]
print(s.count('1'))

# Solution: 5