for x in range(1, 100000):
    s = 3 ** 2000 + 3**10-x
    k = 0
    while s != 0:
        if s % 3 == 2:
            k +=1
        s//=3

    if k == 2000:
        print(x)
