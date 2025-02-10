# https://inf-ege.sdamgia.ru/problem?id=15138

x = 25 ** 6 + 5 ** 18 - 5
s = ""
while x != 0:
    s += str(x % 5)
    x //= 5
s = s[::-1]
print(s.count('4'))

# Solution: 11