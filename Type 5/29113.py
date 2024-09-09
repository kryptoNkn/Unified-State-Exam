#https://inf-ege.sdamgia.ru/problem?id=29113

for n in range(128, 256):
    s = bin(n)[2:]  
    s = str(s)
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r = int(s, 2)  
    if n - r == 185:
        print(n)