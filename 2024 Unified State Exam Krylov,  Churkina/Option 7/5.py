for N in range(10000):
    b = bin(N)[2:]
    if b.count('1') % 2 == 0:
        b = b[:len(b)//2] + '1' + b[len(b)//2:]
    r = int(b,2)
    if r >= 26:
        print(N)
        break
