for N in range(10000):
    b = bin(N)[2:]
    if N % 5 == 0:
        b = b[:3] + b
    else:
        ost = N % 5
        proizv = ost * 5
        b2 = bin(proizv)[2:]
        b += b2
    r = int(b,2)
    if r < 313:
        print(N)

# 35



