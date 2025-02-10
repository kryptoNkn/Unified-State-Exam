for A in range(1, 10000):
    if all((x % A == 0) or ((x in range(70,91)) <= (x % 22 != 0)) for x in range(1, 1000)):
        print(A)