# https://inf-ege.sdamgia.ru/problem?id=13600

x = 4 ** 255 + 2 ** 255 - 255
s = bin(x)[2:]
print(s.count('1'))

# Solution: 249