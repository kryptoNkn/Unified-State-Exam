# Conversion to quaternary number system
def fun(x):
    s = ""
    while x > 0:
        s += str(x % 4)
        x = x // 4
    return s[::-1]

# Algorithm
mx_n = 0
for n in range(1, 10000):
    n4 = fun(n)
    if n % 4 == 0:
        n4 += n4[-2:]
    else:
        n4 += fun((n % 4) * 2)
    R = int(n4, 4)
    if R < 369:
        mx_n = max(mx_n, n)
print(mx_n)

# Solution: 89