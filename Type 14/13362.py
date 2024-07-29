# https://inf-ege.sdamgia.ru/problem?id=13362

x = 125 + 25 ** 3 + 5 ** 9
s = ""
while x != 0:
    s += str(x % 5)
    x //= 5
s = s[::-1]
print(s.count('0'))

# Solution: 7