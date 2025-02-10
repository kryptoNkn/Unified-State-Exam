for N in range(1,10000):
    b = bin(N)[2:]
    if N % 2 == 0:
        b2 = b + '01'
    else:
        b2 = '1' + b +'1'
    r = int(b2,2)
    if r > 156:
        print(N)
# 33