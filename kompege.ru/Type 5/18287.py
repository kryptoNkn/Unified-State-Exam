for N in range(10000):
    b = bin(N)[2:]
    if (b.count('0')+b.count('1')) % 2 == 0:
        b2 = b + '1'
    else:
        b2 = '1' + b + '0'
    r = int(b2,2)
    if r > 666 and r < 1030:
        print(r)
# 1025
