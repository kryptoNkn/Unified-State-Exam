for A in range(1, 10000):
    if all(((x % 12 == 0) <= (x % 42 != 0)) or (x + A >= 4096) for x in range(1, 1000)):
        print(A)
# 4012