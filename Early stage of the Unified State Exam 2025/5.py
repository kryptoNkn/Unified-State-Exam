for n in range(1,1000):
    b = bin(n)[2:]
    if sum(map(int,b))%2==0:
        b_pripis = b+'0'
        b2 = '10'+b_pripis[2:]
    else:
        b_pripis = b + '1'
        b2 = '11' + b_pripis[2:]
    r = int(b2,2)
    if r>480:
        print(n)
        break