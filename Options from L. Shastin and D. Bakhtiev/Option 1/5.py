for n in range(1,10000):
    b = bin(n)[2:]
    summ = sum(map(int,b))
    if summ%2==0:
        b2 = b+'11'
    else:
        b2 = b+'01'
    r = int(b2,2)
    if r>61 and r < 65:
        print(r)
