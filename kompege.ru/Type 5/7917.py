# https://inf-ege.sdamgia.ru/problem?id=7917

for n in range(101, 1001):
    s = str(n)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    first = str(min(k1, k2))
    second = str(max(k1, k2))
    sum = first + second
    if sum == '1115':
        print(n)
        break