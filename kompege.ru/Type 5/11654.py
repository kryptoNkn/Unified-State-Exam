def f(n):
    s = ''
    while n > 0:
        s = str(n%7) + s
        n //= 7
    return s

for n in range(10000):
    b = f(n)
    if b.count('2') % 2 == 0:
        b += '555'
    else:
        b = '1' + b
    r = int(b,7)
    if r < 3799 and r > 3790:
        print(n)
# 1395
