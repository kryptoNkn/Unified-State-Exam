for A in range(1000):
    if all(((x&52!=0) and (x&48==0)) <= (not(x&A==0)) for x in range(100)):
        print(A)
        break