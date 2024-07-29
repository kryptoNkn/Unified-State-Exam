# https://inf-ege.sdamgia.ru/problem?id=11352

x = 9 ** 18 + 3 ** 54 - 9
s = ""
while x != 0:
    s += str(x % 3)
    x //= 3
s = s[::-1]
print(s.count('2'))

# Solution: 34