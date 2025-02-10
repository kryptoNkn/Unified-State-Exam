for x in range(2031):
    n = 6**260+6**160+6**60-x
    count = 0
    while n > 0:
        if n % 6 == 0:
            count+=1
        n//=6

    if count == 202:
        print(x)

# 216