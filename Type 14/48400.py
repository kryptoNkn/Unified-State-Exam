# https://inf-ege.sdamgia.ru/problem?id=48400

for x in range(11):
    t = 2 * 11 ** 0 + x * 11 ** 1 + 5 * 11 ** 2 + 9 * 11 ** 3 + 8 * 12 ** 0 + 5 * 12 **1 + 4 * 12 ** 2 + x * 12 ** 3
    if t % 136 == 0:
        print(t // 136)
        break

# Solution: 174