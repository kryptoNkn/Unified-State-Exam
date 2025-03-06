for A in range(1, 10000):
    if all(((405%x==0) <= (81%x==0)) or (A-x>162) for x in range(1,1000)):
        print(A)
        break