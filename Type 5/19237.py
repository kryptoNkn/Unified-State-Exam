def f(N):
    s=''
    while N != 0:
        s=str(N % 3)+s
        N//=3
    return s

for N in range(1, 10000):
    b = f(N)
    if N % 3==0:
        b = b + b[-2:]
    else:
        b_sum = sum(int(x) for x in b)
        b2 = f(b_sum)
        b = b + b2
    r = int(b,3)
    if r > 220 and r<240:
        print(r)
# 222