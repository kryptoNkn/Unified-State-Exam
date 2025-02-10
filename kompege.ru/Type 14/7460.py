# https://inf-ege.sdamgia.ru/problem?id=7460

x = 4 ** 2014 + 2 ** 2015 - 8
s = bin(x)[2:]
print(s.count('1'))

# Solution: 2013