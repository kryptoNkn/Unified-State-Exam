for N in range(10000):
    b = bin(N)[2:]
    if N % 2 ==0:
        b+='0'
    else:
        b+='1'
    if b.count('1') % 3 == 0:
        b = b[2:]
        b = '11' + b
    else:
        b = b[2:]
        b = '10' + b
    r = int(b,2)
    if r <= 37:
        print(N)

# 25