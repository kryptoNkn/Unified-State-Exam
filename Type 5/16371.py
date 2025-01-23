# 16371

for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        ost = n%3
        mult = ost * 3
        b_konec = bin(mult)[2:]
        b = b + b_konec
    r = int(b,2)
    if r >= 195 and r < 200:
        print(r)