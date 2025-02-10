for n in range(10000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b,2)
    if n <= 12 and n > 10:
        print(r)