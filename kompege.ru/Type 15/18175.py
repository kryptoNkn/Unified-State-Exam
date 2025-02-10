for A in range(1, 10000):
    if all(((x % 7 != 0) and (x % 13 == 0)) <= (x > A - 40) for x in range(1, 1000)):
        print(A)
