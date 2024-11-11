for A in range(10000):
    if all((x+y<=24) or (y<=x-2) or (y >= A) for x in range(1, 1000) for y in range(1,1000)):
        print(A)
# 12