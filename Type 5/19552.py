for N in range(1, 10000):
    b = bin(N)[2:]
    if N % 2 == 0:
        b = b+'100'
    else:
        b=b+'011'
    r = int(b,2)
    if r > 300 and r < 310:
        print(N)