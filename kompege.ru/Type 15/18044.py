for x in range(1, 100):
    M = 32 <= x <= 68
    N = 54 <= x <= 76
    A = False
    print(x, (not((M or N))) == (not(A)))
# 44
