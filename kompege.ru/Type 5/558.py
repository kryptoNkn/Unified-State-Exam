for N in range(10000):
    b = bin(N)[2:]
    b += b[-1]
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'

    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'

    r = int(b,2)
    if r > 97:
        print(N)

# 13