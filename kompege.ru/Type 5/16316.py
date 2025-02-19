for N in range(1, 10000):
    b = bin(N)[2:]
    if N%2==0:
        b_new = b + '10'
    else:
        b_new = '1' + b + '01'
    r = int(b_new,2)

    if r > 516:
        print(N)
        break