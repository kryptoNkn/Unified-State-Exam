for n in range(4, 10000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b2 = b + b[:3]
    else:
        b2 = '1' + b + '01'
    r = int(b2,2)
    if r > 600 and r < 625:
        print(r)