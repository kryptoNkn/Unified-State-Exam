m = 0
for n in range(3, 10001):
    s = '3' + '5' * n
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555','3',1)
        else:
            s = s.replace('333','5',1)
    m = max(m, sum(map(int, s)))
print(m)