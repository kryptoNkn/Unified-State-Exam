for x in range(40,110):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = 48 <= x <= 94
    print(x, (not(C or J)) <= (not(A)))

# 52