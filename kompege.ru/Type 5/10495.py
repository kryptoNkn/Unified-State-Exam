# https://inf-ege.sdamgia.ru/problem?id=10495

for n in range(1,10000):
    s = bin(n)[2:]
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    r = int(s, 2)
    if r > 97:
        print(n)
        break
    
