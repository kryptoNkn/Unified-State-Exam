# https://inf-ege.sdamgia.ru/problem?id=13743

x = 49 ** 10 + 7 ** 30 - 49
s = ""
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]
print(s.count('6'))

# Solution: 18