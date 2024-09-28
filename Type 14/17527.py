for x in range (2031):
    i = 3 ** 100 - x
    count = 0
    while i != 0:
        if i % 3 == 0:
            count += 1
        i //= 3

    if count==5:
        print(x)