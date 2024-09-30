for x in range(2031):
    n = 7 ** 170 + 7 ** 100 - x
    count = 0
    while n != 0:
        if n % 7 == 0:
            count += 1
        n//=7
    if count == 71:
        print(x)

# 2029