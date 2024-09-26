for n in range(10000):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b += '11'
    else:
        b += '01'
    r = int(b,2)
    if r > 61 and r < 65:
        print(r)