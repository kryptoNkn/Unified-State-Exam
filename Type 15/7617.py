for A in range(0, 1000):
    if all((x>=9) or (2*x<y) or (x*y<A) for x in range(0,100) for y in range(0,100)):
        print(A)
    