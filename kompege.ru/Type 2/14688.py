# https://inf-ege.sdamgia.ru/problem?id=14688

print("x y z")
for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x or y) <= (z == x)):
                print(x,y,z)

# Solution: xzy
