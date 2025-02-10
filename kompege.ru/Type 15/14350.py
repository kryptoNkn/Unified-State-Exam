max_A = 0
for A in range(1, 10000):
    if all(((x < 7) or (y >= 3*x + A - 20) or (x >= 34) or (y < 121)) for x in range(0, 1000) for y in range(0, 1000)):
        max_A = A
print(max_A)