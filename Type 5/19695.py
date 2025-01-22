for N in range(1, 10000):
    b = bin(N)[2:]
    if N % 3 == 0:
        b = b+b[-2:]
    else:
        b = '1' + b + '1'
    r = int(b,2)
    if r > 700 and r < 710:
        print(r)
