for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b2 = '10' + b
    else:
        b2 = '1' + b + '01'
    r = int(b2,2)
    if n <= 12 and n > 10:
        print(r)
# 109