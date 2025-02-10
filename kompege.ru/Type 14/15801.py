# https://inf-ege.sdamgia.ru/problem?id=15801

x = 36 ** 7 + + 6 ** 19 - 18
s = ""
while x != 0:
    s += str(x % 6)
    x //= 6
s = s[::-1]
print(s.count("5"))
# Solution: 12