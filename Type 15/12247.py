for A in range(1, 1000):
    if all((x&A==0) or (x&37!=0) or (x&12!=0) for x in range(1, 1000)):
        print(A)
# 45