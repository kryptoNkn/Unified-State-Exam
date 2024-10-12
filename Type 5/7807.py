max_R = 0
best_N = 0

for N in range(1, 10000):
    b = bin(N)[2:]
    if N % 3 == 0:
        dve_pervii_dvoi4 = b[:2]
        b += dve_pervii_dvoi4
    else:
        ost = N % 3
        ost_v_dvoi4 = bin(ost)[2:]
        b += ost_v_dvoi4
    r = int(b, 2)
    if r < 105 and r > max_R:
        max_R = r
        best_N = N

print(best_N)