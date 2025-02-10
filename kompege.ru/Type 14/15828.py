# https://inf-ege.sdamgia.ru/problem?id=15828

x = 36 ** 8 + 6 ** 20 - 12
s = ""
while x != 0:
    s += str(x % 6)
    x //= 6
s = s[::-1]
print(s.count("5"))

# Solution: 14