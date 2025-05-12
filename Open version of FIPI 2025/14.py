for x in range(1,2300):
    n = 7**350+7**150-x
    k=0
    while n!=0:
        if n%7==0:
            k+=1
        n//=7
    
    if k==200:
        print(x)