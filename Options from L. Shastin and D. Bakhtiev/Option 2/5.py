for n in range(1,10000):
    b = bin(n)[2:]
    if n%5==0:
        b2 = b[:3] + b
    else:
        ost=n%5
        umnoj=ost*5
        b_bin = bin(umnoj)[2:]
        b2 = b + b_bin
    r = int(b2,2)
    if n%2!=0 and r < 313:
        print(n)
# 35