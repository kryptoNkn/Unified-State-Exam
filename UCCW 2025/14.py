for x in range(1, 3000):
    n = 4**210+4**110-x
    k=0
    while n!=0:
        if n%4==0:
            k+=1
        n//=4
    if k==105:
        print(x)
        break