def f(n):
    s = ''
    while n != 0:
        s=s+str(n % 12)
        n//=12
    return s[::-1]

for N in range(1,10000):
    b = f(N)
    if N % 4 == 0:
        b2 = '2' + b + '64'
    else:
        perebor = [int(x) for x in b]
        maxx_str = max(perebor)
        maxx = str(maxx_str)
        b2 = b + maxx
    r = int(b2, 12)
    if r > 1799 and r < 1810:
        print(r)