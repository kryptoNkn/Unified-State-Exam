def f(n):
    s = ''
    while n != 0:
        s = str(n%3)+s
        n//=3
    return s

for n in range(1, 10000):
    b = f(n)
    if n % 3 == 0:
        b = b+b[-2:]
    else:
        b = b + f(sum(map(int,b)))
    r = int(b,3)
    if r > 220 and r < 225:
        print(r)