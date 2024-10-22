for x in range(1, 5556):
    n = 5 ** 150 + 5 ** 135 - x
    count = 0
    while n > 0:
        if n % 5 == 4:
            count += 1
        n //= 5

    if count == 134:
        print(x)

# 3126