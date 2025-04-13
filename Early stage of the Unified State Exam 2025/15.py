for A in range(0,1000):
    if all((5<y) or (x>32) or (x+2*y<A) for x in range(100) for y in range(100)):
        print(A)
        break