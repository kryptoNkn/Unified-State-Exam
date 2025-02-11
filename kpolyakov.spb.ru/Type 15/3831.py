for A in range(1, 1001):
    if all((A%7==0) and (240%x==0) <= ((A%x!=0) <= (780%x!=0)) for x in range(1, 100)):
        print(A)

# 2