def f(n):
    s=''
    while n!=0:
        s = str(n%3) + s
        n//=3
    return s

for n in range(9, 10000):
    b3 = f(n)
    if n % 4 == 0:
        b_new = b3 + b3[-3:]
    else:
        b_new = '1' + b3 + '20'
    r = int(b_new,3)
    if r > 423 and r < 440:
        print(r)
