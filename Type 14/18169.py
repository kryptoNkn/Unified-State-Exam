for x in range(100000):
    n = 3**2000+3**10-x
    count = 0
    while n > 0:
        if n % 3 == 2:
            count+=1
        n//=3

    if count == 2000:
        print(x)