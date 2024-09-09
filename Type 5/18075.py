# https://inf-ege.sdamgia.ru/problem?id=18075

for n in range(1, 100000):
    s = bin(n)[2:]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 123:
        print(r)
        break