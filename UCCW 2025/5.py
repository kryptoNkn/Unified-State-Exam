def troi4(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(2, 1000):
    b = troi4(n)
    if n % 3 == 0:
        b2 = b + b[-2:]
    else:
        ost = n % 3
        umnoj = ost * 3
        perevod = troi4(umnoj)
        b2 = b + perevod
    r = int(b2, 3)
    if r <= 150:
        print(n)
# 16