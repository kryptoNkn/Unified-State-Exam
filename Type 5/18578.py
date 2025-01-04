def f(x):
    s = ''
    while x != 0:
        s = str(x % 4) + s
        x//=4
    return s

for N in range(1,10000):
    b4 = f(N)
    if N % 4 == 0:
        bNew = '2' + b4 + '03'
    else:
        bOstatok = N % 4
        b5 = bOstatok * 5
        bPerevod = f(b5)
        bNew = b4 + bPerevod
    r = int(bNew, 4)
    if r <= 567 and r > 550:
        print(N)