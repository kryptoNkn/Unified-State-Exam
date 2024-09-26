for n in range(10000):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b += '0'
        b = b[2:]
        b = '10' + b
    else:
        b += '1'
        b = b[2:]
        b = '11' + b
    r = int(b,2)
    if n > 27 and n < 30:
        print(r)

# 42