for x in range(1, 5555):
    s = 5 ** 150 + 5 **135-x
    k = 0
    while s != 0:
        if s % 5 == 4:
            k+=1
        s//=5

    if k == 134:
        print(x)