arr = []
for x in range(1, 2030):
    s = 6 ** 2030 + 6 ** 100 - x
    k = 0
    while s != 0:
        if s % 6 == 0:
            k+=1
        s//=6
    arr.append(k)
print(max(arr))


