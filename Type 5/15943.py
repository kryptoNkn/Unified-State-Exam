# https://inf-ege.sdamgia.ru/problem?id=15943

for n in range(1, 10000):
    s = bin(n)[2:]
    s = str(s)
    s = s + s[-1]
    s = s + str(s.count("1") % 2)
    r = int(s, 2)
    if r > 105:
        print(r)
        break