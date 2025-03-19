for n in range(1, 10000):
    b = bin(n)[2:]
    summ = sum(map(int,b))
    if summ%2==0:
        b2 = b+'0'
        b_new ='10'+b2[2:]
    else:
        b2 = b+'1'
        b_new = '11'+b2[2:]
    r = int(b_new,2)
    if r>19:
        print(n)
        break
