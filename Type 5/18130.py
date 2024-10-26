box = []
for n in range(10000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = '1' + b
        b = b[:-2] + '11'
    else:
        b = '10' + b + '0'
    r = int(b,2)
    if r > 999 and n % 2 == 0:
        box.append(r)
        print(min(box))
        
        
        
        
        