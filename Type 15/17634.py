for A in range(1000):
    if all((x+y<=30) or (y<=x+2) or (y>=A) for x in range(1,1000) for y in range(1, 1000)):
        print(A)
# 17