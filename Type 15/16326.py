for A in range(1, 10000):
    if all((x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0)) for x in range(1, 1000)):
        print(A)
# 28
