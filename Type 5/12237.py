for n in range(1,10000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b2 = b + b[-2:]
    else:
        b2 = '1' + b + '0'
    r = int(b2,2)
    if r < 100:
        print(n)
# 24