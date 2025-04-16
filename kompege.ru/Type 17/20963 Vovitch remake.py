f = [int(x) for x in open('17.txt')]
arr = []

# c = [x for x in f if len(str(abs(x)))==4 and x%17==0]
# print(min(c)**2)
for i in range(len(f) - 2):
    a = abs(f[i])
    b = abs(f[i + 1])
    c = abs(f[i + 2])

    if (len(str(a)) == 4 and a % 100 == 27) or (len(str(b)) == 4 and b % 100 == 27) or (
            len(str(c)) == 4 and c % 100 == 27):
        if (a ** 2 + b ** 2 + c ** 2) <= 99580441:
            arr.append(a + b + c)
print(len(arr), min(arr))