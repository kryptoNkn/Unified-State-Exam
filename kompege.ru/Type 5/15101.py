# https://inf-ege.sdamgia.ru/problem?id=15101

for n in range(1000, 10000):
    s = str(n)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    second = str(max(k1, k2, k3))
    s1 = first + second
    if s1 == '1215':
        print(n)
        break
