for n in range(10000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b2 = '10' + b + '10'
    else:
        b2 = '1' + b + '00'
    r = int(b2,2)
    if r > 100 and r < 110:
        print(r)