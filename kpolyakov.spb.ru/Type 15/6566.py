for A in range(0, 1000):
    if all((x>=27) or (2*x<3*y) or (A > (x+2)*(y-3)) for x in range(0,100) for y in range(0,100)):
        print(A)
        break