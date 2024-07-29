# https://inf-ege.sdamgia.ru/problem?id=7761

x = 4 ** 2020 + 2 ** 2017 - 15
s = bin(x)[2:]
print(s.count('1'))

# Solution: 2015
