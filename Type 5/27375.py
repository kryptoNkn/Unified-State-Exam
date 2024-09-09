# https://inf-ege.sdamgia.ru/problem?id=27375


for n in range(1, 10000): 
    i = n
    s = ''
    while i>0:
        s+=(str(i%3))
        i //= 3
    s = s[::-1]
    s+=(str(n%3)) 
    s = int(s,3)
    if s > 99: 
        print(s)
        break