for A in range(1, 1000):
    if all(((x%2==0) <= (x%13!=0)) or (x+A>=1000) for x in range(1,100)):
        print(A)
        break