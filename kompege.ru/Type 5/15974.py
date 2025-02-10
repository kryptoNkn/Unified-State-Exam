#https://inf-ege.sdamgia.ru/problem?id=15974

for n in range(10000, 1, -1):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = s + "10"
    else:
        s = s + "01"
    r = int(s, 2)
    if r <= 102:
        print(r)
        break

