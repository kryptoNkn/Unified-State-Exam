# 63051
# https://inf-ege.sdamgia.ru/problem?id=63051

print("x y z w u")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                for u in range(0, 2):
                    if not(((z <= w)and(y == (not(x)))) <= (u == (y or z))):
                        print(x, y, z, w, u)

# Solution: uywzx