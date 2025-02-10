for A in range(10000):
    if all((not(x+y-73>0)) or (not(37-x+y>0)) or (y-A>0) for x in range(1000) for y in range(1000)):
        print(A)