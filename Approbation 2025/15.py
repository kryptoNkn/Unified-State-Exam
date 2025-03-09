B = range(60, 81)  
for A in range(1, 1000):
    if all((x % A == 0) or (x not in B or x % 22 != 0) for x in range(1, 10**5)):
        print(A)