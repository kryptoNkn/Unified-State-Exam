for x in range(10, 100):
    P = 13<=x<=19
    Q = 17<=x<=23
    A = 13 <= x <= 23
    print(x, (not((not(P)) <= Q)) <= (A <= ((not(Q)) <= P)))
# 10