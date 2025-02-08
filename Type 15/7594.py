for A in range(0,1000):
    if all((x&39==0) or ((x&11==0) <= (x&A!=0)) for x in range(0,1000)):
        print(A)
        break