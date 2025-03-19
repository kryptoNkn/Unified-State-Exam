for x in range(2031):
    k=0
    s = 3**100-x
    while s!=0:
        if s%3==0:
            k+=1
        s//=3
    if k==1:
        print(x)
