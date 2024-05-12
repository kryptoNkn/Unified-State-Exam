for A in range(-300, 300):
    flag = False
    for x in range(300):
        for y in range(300):
            if((4 * x + y < A) or (x < y) or (22 <= x)) == 0:
                flag = True
    if flag == False:
        print(A)
        break