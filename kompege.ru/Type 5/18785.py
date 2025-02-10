# https://inf-ege.sdamgia.ru/problem?id=18785

for n in range(1, 100):
    s = bin(n)[2:]
    s = str(s)
    if s[-1] == '0':
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s,2)
    if r > 52:
        print(n)
        break
