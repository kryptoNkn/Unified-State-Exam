for A in range(0, 10000):
    if all((x&57 == 0) or ((x&23 == 0) <= (x&A != 0)) for x in range(1, 1000)):
        print(A)