# https://inf-ege.sdamgia.ru/problem?id=48397

for x in range(0, 13):
    a = 1 * 13 ** 0 + 7 * 13 ** 1 + x * 13 ** 2 + 8 * 13 ** 3 + 15 * 17 ** 0 + 13 * 17 ** 1 + x * 17 ** 2 + 3 * 17 ** 3
    if a % 197 == 0:
        print(a // 197)

# Solution: 175
