for n in range(3, 10000):
    s = '4'+'2'*n
    while '42' in s or '8222' in s or '2222' in s:
        if '42' in s:
            s = s.replace('42','2',1)
        if '8222' in s:
            s = s.replace('8222', '24', 1)
        if '2222' in s:
            s = s.replace('2222', '8', 1)

    summ = sum(map(int,s))
    if summ == 110:
        print(n)
        break